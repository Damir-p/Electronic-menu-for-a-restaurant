from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/guest/', views.guest_login, name='guest_login'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
