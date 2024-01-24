from django.db import models
from django.core.validators import FileExtensionValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class TemplateSettings(models.Model):

    TemplateOne = 'T1'
    TemplateTwo = 'T2'
    TemplateChoice = [
        (TemplateOne, 'Template one'),
        (TemplateTwo, 'Template Two'),
    ]

    template = models.CharField(max_length=2, choices=TemplateChoice, default=TemplateOne)
    website_name = models.CharField(max_length=255, blank=False, null=False)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.template
    

class About(models.Model):
    full_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50)
    title  = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    present_address = models.CharField(max_length=200, blank=True, null=True)
    permanent_address = models.CharField(max_length=200, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    profile_picture = ProcessedImageField(upload_to='profile',
                                           validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
                                           options={'quality': 70},  blank=True, null=True)
    title_background = ProcessedImageField(upload_to='others', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], processors=[ResizeToFill(1240, 755)], options={'quality': 70})
    full_cv = models.FileField(upload_to='cv', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions = ['pdf', 'docx'])])
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.full_name
