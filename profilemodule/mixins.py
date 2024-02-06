# mixins.py
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone
import os
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.utils.html import format_html
from django.apps import apps
from django.forms import DateInput
import math


class GetModel:
    def get_model_by_name(model_name):
        try:
            model = apps.get_model(app_label='profilemodule', model_name=model_name)
            return model
        except LookupError:
            return None

class GetImageFieldName:
    def get_field_name(instance):
        for field in instance._meta.fields:
            if isinstance(field, models.ImageField):
                return field.name

class CheckAdminModel:
    def get_admin_model_status(model_name):
        admin_model = ['user', 'session']
        if model_name in admin_model:
            return False
        else: 
            return True

class CustomAddPermissionMixin:
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return False
        return super().has_add_permission(request)

class CustomGetQuerySetAddPermissionMixin: 
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(created_by=request.user.pk)
            if queryset.count() > 0:
                self.has_add_permission = lambda request: False
            return queryset
        else:
            return queryset 

class CustomGetQuerySetMixin: 
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(created_by=request.user.pk)
            return queryset
        else:
            return queryset 
        
class CustomSaveModelMixin:
    def save_model(self, request, obj, form, change):
        if change:
            existing_obj = self.get_object(request, obj.pk)
            obj.created_at = existing_obj.created_at
            obj.updated_at = timezone.now()
            obj.created_by = existing_obj.created_by
            obj.updated_by = request.user.id
            obj.save()
        else:
            obj.created_by = request.user.id
            obj.save()


class CustomSaveModelOrderNumberMixin:
    def save_model(self, request, obj, form, change):
        model_name = obj._meta.model_name
        instance = GetModel.get_model_by_name(model_name)
        date_calucated_model = ['experience']
        if model_name in date_calucated_model:
            start_date = obj.experience_start_date
            end_date = obj.experience_end_date
            if start_date and not end_date:
                end_date = timezone.now().date()
            if start_date and end_date:
                difference_in_years = math.floor((end_date - start_date).days / 365)
                difference_in_months = math.floor(((end_date - start_date).days % 365) / 30)
            obj.experience_duration_calculated = f"{difference_in_years} yrs & {difference_in_months} months"

        if change:
            existing_obj = self.get_object(request, obj.pk)
            obj.order_number = existing_obj.order_number
            obj.created_at = existing_obj.created_at
            obj.updated_at = timezone.now()
            obj.created_by = existing_obj.created_by
            obj.updated_by = request.user.id
            obj.save()
        else:
            if not obj.order_number:
                last_instance = instance.objects.last()
                obj.order_number = last_instance.pk + 1 if last_instance else 1
            obj.created_by = request.user.id
            obj.save()

 
class SwitchOrderMixin:
    ordering = ['order_number']
    actions = ['switch_order']
    
    def switch_order(self, request, queryset):
        model_name = self.model.__name__
        if queryset.count() == 2:
            order1, order2 = queryset
            order1.order_number, order2.order_number = order2.order_number, order1.order_number
            order1.save()
            order2.save()
            self.message_user(request, f"{model_name}'s ordering switched successfully.")
        else:
            self.message_user(request, f"Please select exactly two {model_name} to switch order numbers.")

class RemoveExistingFilesMixin:
    @receiver(pre_save)
    def delete_existing_image(instance, **kwargs):
        model_name = instance._meta.model_name
        get_instance = GetModel.get_model_by_name(model_name)
        image_field_name = GetImageFieldName.get_field_name(instance)
        get_admin_model_status = CheckAdminModel.get_admin_model_status(model_name)
        if instance.pk and get_admin_model_status:
            old_instance = get_instance.objects.get(pk=instance.pk)
            existing_image = getattr(old_instance, image_field_name)

            if existing_image and existing_image != getattr(instance, image_field_name):
                if os.path.isfile(existing_image.path):
                    os.remove(existing_image.path)

    @receiver(pre_delete)
    def pre_delete_existing_image(instance, **kwargs):
        model_name = instance._meta.model_name
        get_admin_model_status = CheckAdminModel.get_admin_model_status(model_name)
        if get_admin_model_status:
            image_field_name = GetImageFieldName.get_field_name(instance)
            existing_image = getattr(instance, image_field_name)
            if existing_image:
                if os.path.isfile(existing_image.path):
                        os.remove(existing_image.path)

        
class CustomTextEditor:
    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget},
    }

class DateAndTextEditor:
    formfield_overrides = {
        models.DateField: {'widget': DateInput(attrs={'type': 'date'})},
        models.TextField: {"widget": CKEditorWidget},
    }

class CustomShortTextFields:
    def short_text_field(obj, field_name, max_length):
        value = getattr(obj, field_name)
        return format_html(value[:max_length] + '...') if len(value) > max_length else value
    
class RemoveExistingFilesMixinAbout:
    @receiver(pre_save, sender=About)
    def delete_existing_image(sender, instance, **kwargs):
        # Check if the instance has an existing image
        if instance.pk:
            old_instance = sender.objects.get(pk=instance.pk)
            old_profile_picture = old_instance.profile_picture
            old_title_background = old_instance.title_background
            old_full_cv = old_instance.full_cv

            # Check if the image field is being updated
            if old_profile_picture and instance.profile_picture != old_profile_picture:
                # Delete the old image file
                if os.path.isfile(old_profile_picture.path):
                    os.remove(old_profile_picture.path)

            if old_title_background and instance.title_background != old_title_background:
                # Delete the old image file
                if os.path.isfile(old_title_background.path):
                    os.remove(old_title_background.path)

            if old_full_cv and instance.full_cv != old_full_cv:
                # Delete the old image file
                if os.path.isfile(old_full_cv.path):
                    os.remove(old_full_cv.path)
