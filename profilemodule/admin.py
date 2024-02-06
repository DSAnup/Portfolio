from django.contrib import admin
from profilemodule.models import *
from .mixins import *

admin.site.site_header = 'Profile Administration Login'

# Register your models here.

@admin.register(TemplateSettings)
class TemplateSettingsAdmin(CustomAddPermissionMixin, CustomSaveModelMixin, CustomGetQuerySetAddPermissionMixin, admin.ModelAdmin):
    fields = ['template', 'website_name']
    list_display = ['template', 'website_name']
    ordering = ['pk']
    
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser: 
            return ['website_name']
        else:
            return []

@admin.register(About)
class AboutAdmin(CustomAddPermissionMixin, CustomSaveModelMixin, CustomGetQuerySetAddPermissionMixin, RemoveExistingFilesMixinAbout, CustomTextEditor, admin.ModelAdmin):
    
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

    list_display = ['full_name', 'designation', 'mobile', 'title', 'email']

@admin.register(SocialPlatform)
class SocialPlatformAdmin(CustomAddPermissionMixin, CustomSaveModelOrderNumberMixin, CustomGetQuerySetMixin, RemoveExistingFilesMixin, SwitchOrderMixin, admin.ModelAdmin):
    
    fields = ['social_platform_name', 'social_platform_icon', 'social_platform_url']
    list_display = ['social_platform_name', 'view_url']

    def view_url(self, obj):
        return format_html('<a href="{}" target="_blank">Click Here</a>'.format(obj.social_platform_url))
    
    view_url.short_description = "Social Link"


@admin.register(Experience)
class ExperienceAdmin(CustomAddPermissionMixin, CustomSaveModelOrderNumberMixin, CustomGetQuerySetMixin, DateAndTextEditor,  RemoveExistingFilesMixin, SwitchOrderMixin, admin.ModelAdmin):
    
    fields = ['experience_title', 'experience_from', 'experience_from_logo', 'experience_start_date', 'experience_end_date', 'experience_duration', 'experience_details' ]
    list_display = ['experience_title', 'experience_from', 'experience_duration']


@admin.register(Education)
class EducationAdmin(CustomAddPermissionMixin, CustomSaveModelOrderNumberMixin, CustomGetQuerySetMixin, RemoveExistingFilesMixin, SwitchOrderMixin, admin.ModelAdmin):
    
    fields = ['education_title', 'education_institution_name', 'education_institution_location', 'education_institution_logo', 'education_institution_url', 'education_duration']
    list_display = ['education_title', 'education_institution_name', 'education_institution_location']

@admin.register(Skill)
class SkillAdmin(CustomAddPermissionMixin, CustomGetQuerySetMixin, CustomSaveModelOrderNumberMixin, RemoveExistingFilesMixin, SwitchOrderMixin, admin.ModelAdmin):
    
    fields = ['skill_name', 'skill_image', 'skill_progress']
    list_display = ['skill_name', 'display_image']
    
    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.skill_image.url))

    display_image.short_description = 'Logo'

@admin.register(Certification)
class CertificationAdmin(CustomAddPermissionMixin, CustomSaveModelOrderNumberMixin, CustomGetQuerySetMixin, RemoveExistingFilesMixin, SwitchOrderMixin, admin.ModelAdmin):
    
    fields = ['certification_title', 'certification_image', 'certification_host', 'certification_url']
    list_display = ['certification_title', 'certification_host', 'view_url']

    def view_url(self, obj):
        return format_html('<a href="{}" target="_blank">Click Here</a>'.format(obj.certification_url))
    
    view_url.short_description = "Certificate Url"


@admin.register(Publication)
class PublicationAdmin(CustomAddPermissionMixin, CustomSaveModelOrderNumberMixin, CustomGetQuerySetMixin, CustomTextEditor, SwitchOrderMixin, admin.ModelAdmin):
    
    fields = ['publication_type', 'publication_url', 'publication_details']
    list_display = ['publication_type', 'publication_url']
    
    def view_url(self, obj):
        return format_html('<a href="{}" target="_blank">Click Here</a>'.format(obj.publication_url))
    
    view_url.short_description = "Publication Url"


@admin.register(Conference)
class ConferenceAdmin(CustomAddPermissionMixin, CustomSaveModelOrderNumberMixin, CustomGetQuerySetMixin, CustomTextEditor, SwitchOrderMixin, admin.ModelAdmin):
    
    fields = ['conference_details']
    list_display = ['short_text_fields']

    def short_text_fields(self, obj):
        return CustomShortTextFields.short_text_field(obj, 'conference_details', 150)
    
    short_text_fields.short_description = 'Conferenece Details'


@admin.register(Training)
class TrainingAdmin(CustomAddPermissionMixin, CustomSaveModelOrderNumberMixin, CustomGetQuerySetMixin, CustomTextEditor, SwitchOrderMixin, admin.ModelAdmin):
    
    fields = ['training_type', 'training_details']
    list_display = ['training_type', 'short_text_fields']

    def short_text_fields(self, obj):
        return CustomShortTextFields.short_text_field(obj, 'training_details', 100)
    
    short_text_fields.short_description = 'Training Details'


@admin.register(Award)
class AwardAdmin(CustomAddPermissionMixin, CustomSaveModelOrderNumberMixin, CustomGetQuerySetMixin, CustomTextEditor, SwitchOrderMixin, admin.ModelAdmin):
    
    fields = ['award_details']
    list_display = ['short_text_fields']

    def short_text_fields(self, obj):
        return CustomShortTextFields.short_text_field(obj, 'award_details', 150)
    
    short_text_fields.short_description = 'Award Details'

