from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('applications/', views.application1, name='Step1'),
    path('applications2/', views.application2, name='Step2'),
    path('applications3/', views.application3, name='Step3'),
    path('applications4/', views.application4, name='Step4'),
    path('applications5/', views.application5, name='Step5'),
    path('yfirfara/', views.yfirfara, name='yfirfara'),
    path('mottekid/', views.mottekinUmsokn, name='mottekid'),
    path('changeProfiles/', views.changeProfiles1, name='changeProfile1'),
    path('changeProfiles2/', views.changeProfiles2, name='changeProfile2'),
    path('changeProfiles3/', views.changeProfiles3, name='changeProfile3'),
    path('changeProfiles4/', views.changeProfiles4, name='changeProfile4')
]
