from django.urls import path
from . import views

urlpatterns = [
  path('', views.test_home, name = 'test_home'),
  path('t1', views.t1, name = 't1'),
  path('t2', views.t2, name = 't2'),
]