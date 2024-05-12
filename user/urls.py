from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('login', LoginView.as_view(template_name="user/login.html"), name='user-login'),
    path('logout', LogoutView.as_view(next_page='user-login'), name='user-logout'),
    path('signup', views.signup, name='user-signup'),
    path('profile', views.profile, name='user-profile')
]