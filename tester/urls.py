from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
  path('', views.test_home, name = 'test_home'),
  path('t1', views.t1, name = 't1'),
  path('post_list', login_required(views.PostList.as_view()) , name = 'post_list'), #T2 list
  path('post_list/<str:pk>', login_required(views.PostDetail.as_view()) , name = 'post_detail'), #T2 detail
  path('post_update/<str:pk>', login_required(views.PostUpdate.as_view()) , name = 'post_update'), #T2 update
  path('post_delete/<str:pk>', login_required(views.PostDelete.as_view()) , name = 'post_delete'), #T2 delete
  path('post_list/create/', login_required(views.PostCreate.as_view()) , name = 'post_create'), #T3 create
  path('t3', views.t3, name = 't3'),
]


  # path('t2', views.t2, name = 't2'),
  # path('t2/<str:pk>/', views.t2_1, name = 't2_1'),