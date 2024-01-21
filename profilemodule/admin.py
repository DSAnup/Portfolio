from django.contrib import admin
from django.utils import timezone
from profilemodule.models import *
from ckeditor.widgets import CKEditorWidget

# Register your models here.
admin.site.site_header = 'Profile Administration Login'

@admin.register(TemplateSettings)
class TemplateSettingsAdmin(admin.ModelAdmin):
    fields = ['template', 'website_name']
    list_display = ['template', 'website_name']
    ordering = ['pk']

    def save_model(self, request, obj, form, change):
        if change:
            existing_obj = TemplateSettings.objects.get(pk=obj.pk)
            obj.created_at = existing_obj.created_at
            obj.updated_at = timezone.now()
            obj.created_by = existing_obj.created_by
            obj.updated_by = request.user.id
            obj.save()
        else:
            obj.created_by = request.user.id
            obj.save()

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    
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
   