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

    def __str__(self):
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

    def __str__(self):
        return self.full_name
    
class SocialPlatform(models.Model):

    social_platform_name = models.CharField(max_length=50)
    social_platform_icon = models.CharField(max_length=50,  blank=True, null=True)
    social_platform_url = models.CharField(max_length=70,  blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.social_platform_name
    
class Experience(models.Model):

    experience_title = models.CharField(max_length= 50)
    experience_from = models.CharField(max_length= 100)
    experience_from_logo = ProcessedImageField(upload_to='experience', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], options={'quality': 80},  blank=True, null=True, processors=[ResizeToFill(64, 64)])
    experience_duration = models.CharField(max_length= 70, blank=True, null=True)
    experience_details = models.TextField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.experience_title
    
class Education(models.Model):

    education_title = models.CharField(max_length=50)
    education_institution_name = models.CharField(max_length=100, blank=True, null=True)
    education_institution_location = models.CharField(max_length=150, blank=True, null=True)
    education_institution_logo = ProcessedImageField(upload_to='education', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], options={'quality': 80}, processors=[ResizeToFill(64, 64)])
    education_institution_url = models.CharField(max_length=70)
    education_duration = models.CharField(max_length=70)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.education_title

class Skill(models.Model):

    skill_name = models.CharField(max_length=50)
    skill_image = ProcessedImageField(upload_to='skill', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], options={'quality': 80}, processors=[ResizeToFill(23, 23)])
    skill_progress = models.PositiveSmallIntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.skill_name
    
class Certification(models.Model):

    certification_title = models.CharField(max_length=50)
    certification_image = ProcessedImageField(upload_to='certification', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], options={'quality': 80}, processors=[ResizeToFill(250, 200)])
    certification_host = models.CharField(max_length=70, blank=True, null=True)
    certification_url = models.CharField(max_length=70, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.certification_title
    
class Publication(models.Model):

    Published = 'P'
    Upcoming = 'U'
    PublicationTypeChoice = [
        (Published, 'Published'),
        (Upcoming, 'Upcoming')
    ]

    publication_type = models.CharField(max_length=2, choices=PublicationTypeChoice, default=Published)
    publication_url = models.CharField(max_length=70, blank=True, null=True)
    publication_details = models.TextField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.publication_details[:10]

class Conference(models.Model):
    
    conference_details = models.TextField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.conference_details[:10]

class Training(models.Model):
    
    Training = 'T'
    Skill = 'S'
    TrainingTypeChoice = [
        (Training, 'Training'),
        (Skill, 'Skill')
    ]

    training_type = models.CharField(max_length=2, choices = TrainingTypeChoice, default = Training)
    training_details = models.TextField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.training_type

class Award(models.Model):
    
    award_details = models.TextField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.award_details[:10]
