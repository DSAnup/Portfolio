# mixins.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
import os
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.utils.html import format_html

class CustomAddPermissionMixin:
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return False
        return super().has_add_permission(request)

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

class CustomGetQuerySetMixin: 
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(created_by=request.user.pk)
            if queryset.count() > 0:
                self.has_add_permission = lambda request: False
            return queryset
        else:
            return queryset 
        
class CustomTextEditor:
    formfield_overrides = {
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
                       
class RemoveExistingFilesMixinSocialPlatform:
    @receiver(pre_save, sender=SocialPlatform)
    def delete_existing_image(sender, instance, **kwargs):
        # Check if the instance has an existing image
        if instance.pk:
            old_instance = sender.objects.get(pk=instance.pk)
            old_file = old_instance.social_platform_icon

            if old_file and instance.social_platform_icon != old_file:
                # Delete the old image file
                if os.path.isfile(old_file.path):
                    os.remove(old_file.path)    

class RemoveExistingFilesMixinSkill:
    @receiver(pre_save, sender=Skill)
    def delete_existing_image(sender, instance, **kwargs):
        # Check if the instance has an existing image
        if instance.pk:
            old_instance = sender.objects.get(pk=instance.pk)
            old_file = old_instance.skill_image

            if old_file and instance.skill_image != old_file:
                # Delete the old image file
                if os.path.isfile(old_file.path):
                    os.remove(old_file.path)    

class RemoveExistingFilesMixinCertification:
    @receiver(pre_save, sender=Certification)
    def delete_existing_image(sender, instance, **kwargs):
        # Check if the instance has an existing image
        if instance.pk:
            old_instance = sender.objects.get(pk=instance.pk)
            old_file = old_instance.certification_image

            if old_file and instance.certification_image != old_file:
                # Delete the old image file
                if os.path.isfile(old_file.path):
                    os.remove(old_file.path)

class RemoveExistingFilesMixinExperience:
    @receiver(pre_save, sender=Experience)
    def delete_existing_image(sender, instance, **kwargs):
        # Check if the instance has an existing image
        if instance.pk:
            old_instance = sender.objects.get(pk=instance.pk)
            old_file = old_instance.experience_from_logo

            if old_file and instance.experience_from_logo != old_file:
                # Delete the old image file
                if os.path.isfile(old_file.path):
                    os.remove(old_file.path)

class RemoveExistingFilesMixinEducation:
    @receiver(pre_save, sender=Education)
    def delete_existing_image(sender, instance, **kwargs):
        # Check if the instance has an existing image
        if instance.pk:
            old_instance = sender.objects.get(pk=instance.pk)
            old_file = old_instance.education_institution_logo

            if old_file and instance.education_institution_logo != old_file:
                # Delete the old image file
                if os.path.isfile(old_file.path):
                    os.remove(old_file.path)