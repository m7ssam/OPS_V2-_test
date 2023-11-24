from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'project_home'),
    path('create-project', views.create_project, name = 'create_project'),
]