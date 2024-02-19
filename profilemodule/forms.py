from django import forms
from .models import *

class MessageForm(forms.ModelForm):
    class Meta:
        model = MyMessage
        fields = ['name', 'email', 'message', 'host_name', 'subject']