from django.contrib import admin
from django.utils import timezone
from profilemodule.models import *
from ckeditor.widgets import CKEditorWidget
from .mixins import *

# Register your models here.
admin.site.site_header = 'Profile Administration Login'

@admin.register(TemplateSettings)
class TemplateSettingsAdmin(CustomSaveModelMixin, admin.ModelAdmin):
    fields = ['template', 'website_name']
    list_display = ['template', 'website_name']
    ordering = ['pk']
    readonly_fields = []

    def get_queryset(self, request):
        # Customize the queryset based on your condition
        queryset = super().get_queryset(request)
        if request.user.username == 'anup':
            queryset = queryset.filter(website_name='anupmondal.me')
            self.readonly_fields += ['website_name']
            if queryset.count() > 0:
                self.has_add_permission = lambda request: False
            return queryset
        elif request.user.username == 'pronoy':
            queryset = queryset.filter(website_name='pronoymondal.me')
            self.readonly_fields += ['website_name']
            if queryset.count() > 0:
                self.has_add_permission = lambda request: False
            return queryset
        else:
            return queryset      

@admin.register(About)
class AboutAdmin(CustomAddPermissionMixin, CustomSaveModelMixin, CustomGetQuerySetMixin, admin.ModelAdmin):
    
    fieldsets = (
        (
            'Basic Information',
            {
                'fields': ['full_name', 'designation', 'mobile', 'title', 'email', 'present_address', 'permanent_address']
            }
         ),
         (
            'Advanced Information',
            {
                'fields': ['about_me', 'profile_picture', 'full_cv', 'title_background']
            }
         ),
    )  

    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget},
    }

    list_display = ['full_name', 'designation']