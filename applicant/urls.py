from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('applicants/', views.application1, name='application1')
]
