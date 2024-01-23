# mixins.py
from django.utils import timezone
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

