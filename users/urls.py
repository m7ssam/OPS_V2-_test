from django.urls import path, include
from . import views

urlpatterns = [
        path('login', views.login, name = 'login'),
        path('sign-up', views.sign_up, name = 'sign_up'),
        path("", include("django.contrib.auth.urls")),
]


