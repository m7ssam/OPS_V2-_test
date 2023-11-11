from django.urls import path, include
from . import views

urlpatterns = [
        path('login', views.login, name = 'login'),
        path('', views.home, name = 'home'),
        path('sign-up', views.sign_up, name = 'sign_up'),
        path('invalid_user', views.invalid_user, name = 'invalid_user'),
        path("", include("django.contrib.auth.urls")),
]


