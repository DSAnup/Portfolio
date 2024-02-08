from django.shortcuts import render
from django.contrib.auth.models import User
from profilemodule.models import *
from pprint import pprint


# Create your views here.
def index(request):
    localuser = 'anup'
    if localuser == 'anup':
        user = User.objects.get(username='anup')
        about = About.objects.get(created_by = user.id)
        socialplatforms = SocialPlatform.objects.filter(created_by = user.id).order_by('order_number')
        experiences = Experience.objects.filter(created_by = user.id).order_by('order_number')
        educations = Education.objects.filter(created_by = user.id).order_by('order_number')
        skills = Skill.objects.filter(created_by = user.id).order_by('order_number')
        certifications = Certification.objects.filter(created_by = user.id).order_by('order_number')
        data = {
            'about': about,
            'socialplatforms': socialplatforms,
            'experiences': experiences,
            'skills': skills,
            'certifications': certifications,
            'educations': educations,
        }
        return render(request, "core/index.html", data)
    else:
        return render(request, "core/index2.html")
