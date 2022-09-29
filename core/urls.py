from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('setting', views.setting, name = 'setting'),
    path('upload', views.upload, name = 'upload'),
    path('follow', views.follow, name = 'follow'),
    path('search', views.search, name = 'search'),
    path('profile/<str:pk>', views.profile, name = 'profile'),
    path('like_post', views.like_post, name = 'like_post'),
    path('signup/', views.signup, name = 'signup'),
    path('signin', views.signin, name = 'signin'),
    path('logout', views.logout, name = 'logout'),
]
