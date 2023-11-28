from django import forms
from django.contrib.auth.models import User
from .models import T1, T2

class T1Form(forms.ModelForm):
  class Meta:
    model = T1
    fields = ['id','a','b','c']
  d = forms.CharField(max_length=10)
    