from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def say_hello(request):
    x = 1
    y = 2
    return render(request, "core/index.html", {'name': x})

def index2(request):
    return render(request, "core/index2.html")
