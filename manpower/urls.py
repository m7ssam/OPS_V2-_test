from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
        path('', views.mp_home, name = 'mp_home'),
        path('mp_list/', views.mp_list, name = 'mp_list'),
        path('mp_move_list', views.mp_move_list, name = 'mp_move_list'),
        path('mp_move', views.mp_move, name = 'mp_move'),
        path('created', views.created, name = 'created'),
        path('error', views.error, name = 'error'),
        path('something_went_wrong', views.something_went_wrong, name = 'something_went_wrong'),
        path('user_page/<str:pk>/', views.user_page, name = 'user_page'),
        path('mplist', login_required(views.MpList.as_view()) , name = 'mplist'),
        path('mphistory', login_required(views.Mp_history_view.as_view()) , name = 'mphistory'),
]