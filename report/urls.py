from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'report_home'),
    path('Project_home', views.Project_home, name = 'Project_home'),
    path('report', views.report, name = 'project_report'),
    path('project_contract', views.project_contract, name = 'project_contract'),
]