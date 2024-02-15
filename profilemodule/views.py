from django.shortcuts import render
from django.contrib.auth.models import User
from profilemodule.models import *
from pprint import pprint
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    host_name = request.get_host()
    if host_name == 'anupmondal.me':
        localuser = 'anup'
        user = get_object_or_404(User, username=localuser)
        about = get_object_or_404(About, created_by = user.id)
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
            'hostname': host_name,
        }
        return render(request, "core/index.html", data)
    
    elif host_name == '127.0.0.1:8000':
        localuser = 'anup'
        user = get_object_or_404(User, username=localuser)
        about = get_object_or_404(About, created_by = user.id)
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
            'hostname': host_name,
        }
        return render(request, "core/index2.html", data)
    
    elif host_name == 'pronoymondal.me':
        localuser = 'pronoy'
        user = get_object_or_404(User, username=localuser)
        about = get_object_or_404(About, created_by = user.id)
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
            'hostname': host_name,
        }
        return render(request, "core/index2.html", data)
    
    else:
        localuser = 'anup'
        user = get_object_or_404(User, username=localuser)
        about = get_object_or_404(About, created_by = user.id)
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
            'hostname': host_name,
        }
        return render(request, "core/index.html", data)
