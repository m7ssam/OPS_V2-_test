from django import forms
from django.contrib.auth.models import User
from .models import Name


class PostProject(forms.ModelForm):
  class Meta:
    model = Name
    fields = ['recipient','project_name','photo']


   