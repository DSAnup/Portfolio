import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from profilemodule.models import *
from django.contrib import messages
from .forms import *


# Create your views here.
def index(request):
    host_name = request.get_host()
    if host_name == 'anupmondal.me':
        localuser = 'anup'
        user = User.objects.get(username=localuser)
        abouts = About.objects.filter(created_by = user.id)
        socialplatforms = SocialPlatform.objects.filter(created_by = user.id).order_by('order_number')
        experiences = Experience.objects.filter(created_by = user.id).order_by('order_number')
        educations = Education.objects.filter(created_by = user.id).order_by('order_number')
        skills = Skill.objects.filter(created_by = user.id).order_by('order_number')
        certifications = Certification.objects.filter(created_by = user.id).order_by('order_number')
        messages_to_display = messages.get_messages(request)
        data = {
            'abouts': abouts,
            'socialplatforms': socialplatforms,
            'experiences': experiences,
            'skills': skills,
            'certifications': certifications,
            'educations': educations,
            'host_name' : host_name,
            'message' : messages_to_display
        }
        return render(request, "core/index.html", data)
    
    elif host_name == 'pronoymondal.me':
        localuser = 'pronoy'
        user = User.objects.get(username=localuser)
        abouts = About.objects.filter(created_by = user.id)
        socialplatforms = SocialPlatform.objects.filter(created_by = user.id).order_by('order_number')
        experiences = Experience.objects.filter(created_by = user.id).order_by('order_number')
        educations = Education.objects.filter(created_by = user.id).order_by('order_number')
        publications = Publication.objects.filter(created_by = user.id).order_by('order_number')
        conferences = Conference.objects.filter(created_by = user.id).order_by('order_number')
        trainings = Training.objects.filter(created_by = user.id).order_by('order_number')
        awards = Award.objects.filter(created_by = user.id).order_by('order_number')
        messages_to_display = messages.get_messages(request)
        data = {
            'abouts': abouts,
            'socialplatforms': socialplatforms,
            'experiences': experiences,
            'conferences': conferences,
            'trainings': trainings,
            'educations': educations,
            'publications': publications,
            'awards': awards,
            'host_name' : host_name,
            'message' : messages_to_display
        }
        return render(request, "core/index2.html", data)
    
    else:
        localuser = 'anup'
        user = User.objects.get(username=localuser)
        abouts = About.objects.filter(created_by = user.id)
        socialplatforms = SocialPlatform.objects.filter(created_by = user.id).order_by('order_number')
        experiences = Experience.objects.filter(created_by = user.id).order_by('order_number')
        educations = Education.objects.filter(created_by = user.id).order_by('order_number')
        skills = Skill.objects.filter(created_by = user.id).order_by('order_number')
        certifications = Certification.objects.filter(created_by = user.id).order_by('order_number')
        messages_to_display = messages.get_messages(request)
        data = {
            'abouts': abouts,
            'socialplatforms': socialplatforms,
            'experiences': experiences,
            'skills': skills,
            'certifications': certifications,
            'educations': educations,
            'host_name' : host_name,
            'message' : messages_to_display
        }
        return render(request, "core/index.html", data)

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Message Send Successfully.')
        return redirect(index)
    
def update_data(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        id = json_data.get('pk')
        read_status = json_data.get('read_status')
        obj = MyMessage.objects.get(pk=id)
        obj.read_status = read_status
        obj.save()
        return JsonResponse({'success': True, 'pk': json_data})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
