from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import CustomLoginView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
