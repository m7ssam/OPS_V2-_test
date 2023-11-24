from django.urls import path
from . import views

urlpatterns = [
        path('', views.mp_home, name = 'mp_home'),
        path('mp_list/', views.mp_list, name = 'mp_list'),
        path('mp_meta', views.mp_meta, name = 'mp_meta'),
        path('mp_move', views.mp_move, name = 'mp_move'),
        path('error', views.error, name = 'error'),
        path('something_went_wrong', views.something_went_wrong, name = 'something_went_wrong'),
        path('user_page/<str:pk>/', views.user_page, name = 'user_page'),
]