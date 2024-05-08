from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('login/', views.login, name='home-login'),
    path('signup/', views.signup, name='home-signup'),
    path('about_us/', views.about_us, name='home-about_us')
]
