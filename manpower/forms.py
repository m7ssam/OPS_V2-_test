from django import forms
from django.contrib.auth.models import User
from .models import Mp_Location


class Mp_move(forms.ModelForm):
  class Meta:
    model = Mp_Location
    fields = ['id','recipient']


   