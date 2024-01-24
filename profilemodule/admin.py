from django.contrib import admin
from profilemodule.models import *
from ckeditor.widgets import CKEditorWidget
from .mixins import *

# Register your models here.
admin.site.site_header = 'Profile Administration Login'

@admin.register(TemplateSettings)
class TemplateSettingsAdmin(CustomAddPermissionMixin, CustomSaveModelMixin, CustomGetQuerySetMixin, admin.ModelAdmin):
    fields = ['template', 'website_name']
    list_display = ['template', 'website_name']
    ordering = ['pk']
    
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser: 
            return ['website_name']
        else:
            return []

@admin.register(About)
class AboutAdmin(CustomAddPermissionMixin, CustomSaveModelMixin, CustomGetQuerySetMixin, RemoveExistingFilesMixinAbout, admin.ModelAdmin):
    
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