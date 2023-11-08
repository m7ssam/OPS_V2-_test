from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('Documentation', views.Documentation, name = 'Documentation'),
    path('underconstruction', views.underconstruction, name = 'underconstruction'),
]