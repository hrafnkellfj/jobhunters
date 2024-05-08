from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('applications/', views.application1, name='Step1'),
    path('applications2/', views.application2, name='Step2'),
    path('applications3/', views.application3, name='Step3'),
    path('applications4/', views.application4, name='Step4'),
    path('applications5/', views.application5, name='Step5'),
    path('motekid/', views.mottekinUmsokn, name='motekid')
]
