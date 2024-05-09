
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('about_us/', views.about_us, name='home-about_us')
]
