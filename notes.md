3
To edit the user registration form in Django to have an id instead of username, you must create a custom registration form.

Then, update the REGISTRATION_FORM variable in your project's settings.py file to point to your custom form. Finally, update your login and logout URLs to use your custom form as the login and logout forms.

Here are the steps on how to do this:

Create a custom registration form. This form should have an extra field for the user's id. You can do this by adding the following code to your forms.py file:
Python
from django import forms
from django.contrib.auth.models import User

class CustomRegistrationForm(forms.ModelForm):
    id = forms.IntegerField(label="ID")

    def clean_id(self):
        id = self.cleaned_data['id']
        try:
            User.objects.get(id=id)
        except User.DoesNotExist:
            raise forms.ValidationError("Invalid ID")
        return id

    def clean(self):
        cleaned_data = super(CustomRegistrationForm, self).clean()
        id = cleaned_data.get('id')
        username = cleaned_data.get('username')
        if id and username:
            raise forms.ValidationError("Please enter only one of ID or username")
        return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'id']
Use code with caution. Learn more
Update the REGISTRATION_FORM variable in your project's settings.py file to point to your custom form. You can do this by adding the following code to your settings.py file:
Python
REGISTRATION_FORM = 'app.forms.CustomRegistrationForm'
Use code with caution. Learn more
Update your login and logout URLs to use your custom form as the login and logout forms. You can do this by adding the following code to your urls.py file:
Python
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login', {'form_class': CustomRegistrationForm}),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
Use code with caution. Learn more
Finally, update your login template to include the extra field for the user's id. You can do this by adding the following code to your login.html file:

HTML
<form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    <label for="id">ID:</label>
    <input type="text" id="id" name="id" value="" />
    <label
 
for="username">Username:</label>

    
<input
 
type="text"
 
id="username"
 
name="username"
 
value="" />

    
<label
 
for="password">Password:</label>

    
<input
 
type="password"
 
id="password"
 
name="password"
 
value="" />

    
<input
 
type="submit"
 
value="Login" />
</form>
Use code with caution. Learn more
This should update the user registration form in Django to have an id instead of username. The id must be in an existing model in the users app named User.id.