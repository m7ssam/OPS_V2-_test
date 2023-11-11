from django.urls import path, include
from . import views

urlpatterns = [
        path('login', views.login, name = 'login'),
        path('logout', views.logout, name = 'logout'),
        path('', views.home, name = 'home'),
        path('sign-up', views.sign_up, name = 'sign_up'),
        path('created', views.created, name = 'created'),
        path('invalid_user', views.invalid_user, name = 'invalid_user'),
        path('dublication', views.dublication, name = 'dublication'),
        path("", include("django.contrib.auth.urls")),
        path('change_password', views.password_change, name = 'password_change'),
]


