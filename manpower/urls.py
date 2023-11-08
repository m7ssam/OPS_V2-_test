from django.urls import path
from . import views

urlpatterns = [
        path('', views.mp_home, name = 'mp_home'),
        path('mp_list', views.mp_list, name = 'mp_list'),
        path('mp_meta', views.mp_meta, name = 'mp_meta'),
]