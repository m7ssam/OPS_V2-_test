from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'report_home'),
    path('report', views.report, name = 'project_report'),
]