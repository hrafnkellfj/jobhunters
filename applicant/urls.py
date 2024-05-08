from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('applications/', views.application1, name='application1'),
    path('applications2/', views.application2, name='application2')
]
