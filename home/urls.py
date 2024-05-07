from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('login/', views.login, name='home-login'),
    path('signup/', views.signup, name='home-signup'),
]