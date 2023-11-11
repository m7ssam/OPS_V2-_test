from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    id = forms.IntegerField(required=True)
    class Meta:
        model = User
        fields = ["id", "password1", "password2"]
        field_order = ["id", "password1", "password2"]
        
