from django.contrib import admin
from profilemodule.models import *
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
class AboutAdmin(CustomAddPermissionMixin, CustomSaveModelMixin, CustomGetQuerySetMixin, RemoveExistingFilesMixinAbout, CustomTextEditor, admin.ModelAdmin):
    
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

    list_display = ['full_name', 'designation', 'about_me_short', 'display_image']

    def about_me_short(self, obj):
        return CustomShortTextFields.short_text_field(obj, 'about_me', 50)
    
    about_me_short.short_description = 'About Me'

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.profile_picture.url))

    display_image.short_description = 'Image'

@admin.register(SocialPlatform)
class SocialPlatformAdmin(CustomAddPermissionMixin, admin.ModelAdmin):
    
    fields = ['social_platform_name', 'social_platform_icon', 'social_platform_url']
    list_display = ['social_platform_name', 'social_platform_icon', 'social_platform_url']


@admin.register(Experience)
class ExperienceAdmin(CustomAddPermissionMixin, CustomTextEditor, admin.ModelAdmin):
    
    fields = ['experience_title', 'experience_from', 'experience_from_logo', 'experience_duration', 'experience_details']
    list_display = ['experience_title', 'experience_from', 'experience_from_logo', 'experience_duration', 'experience_details']


@admin.register(Education)
class EducationAdmin(CustomAddPermissionMixin, admin.ModelAdmin):
    
    fields = ['education_title', 'education_institution_name', 'education_institution_location', 'education_institution_logo', 'education_institution_url', 'education_duration']
    list_display = ['education_title', 'education_institution_name']

@admin.register(Skill)
class SkillAdmin(CustomAddPermissionMixin, admin.ModelAdmin):
    
    fields = ['skill_name', 'skill_image', 'skill_progress']
    list_display = ['skill_name', 'skill_image']

@admin.register(Certification)
class CertificationAdmin(CustomAddPermissionMixin, admin.ModelAdmin):
    
    fields = ['certification_title', 'certification_image', 'certification_host', 'certification_url']
    list_display = ['certification_title', 'certification_image']


@admin.register(Publication)
class PublicationAdmin(CustomAddPermissionMixin, CustomTextEditor, admin.ModelAdmin):
    
    fields = ['publication_type', 'publication_url', 'publication_details']
    list_display = ['publication_type', 'publication_url']


@admin.register(Conference)
class ConferenceAdmin(CustomAddPermissionMixin, CustomTextEditor, admin.ModelAdmin):
    
    fields = ['conference_details']
    list_display = ['conference_details']


@admin.register(Training)
class TrainingAdmin(CustomAddPermissionMixin, CustomTextEditor, admin.ModelAdmin):
    
    fields = ['training_type', 'training_details']
    list_display = ['training_type', 'training_details']


@admin.register(Award)
class AwardAdmin(CustomAddPermissionMixin, CustomTextEditor, admin.ModelAdmin):
    
    fields = ['award_details']
    list_display = ['award_details']

