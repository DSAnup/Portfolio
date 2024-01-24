# mixins.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
import os
from .models import *

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

class RemoveExistingFilesMixinAbout:
    @receiver(pre_save, sender=About)
    def delete_existing_image(sender, instance, **kwargs):
        # Check if the instance has an existing image
        if instance.pk:
            old_instance = About.objects.get(pk=instance.pk)
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
