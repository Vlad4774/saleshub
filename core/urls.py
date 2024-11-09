from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_started, name='get_started'),
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('base/', views.base, name='base')
]
