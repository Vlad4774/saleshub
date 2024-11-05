from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('getStarted/', views.get_started, name='get_started'),
    path('login/', views.login, name='login')
]
