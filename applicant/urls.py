from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('applications/<int:jobid>', views.application1, name='Step1'),
    path('applications2/<int:jobid>', views.application2, name='Step2'),
    path('applications3/<int:jobid>', views.application3, name='Step3'),
    path('applications4/<int:jobid>', views.application4, name='Step4'),
    path('applications5/<int:jobid>', views.application5, name='Step5'),
    path('yfirfara/', views.yfirfara, name='yfirfara'),
    path('mottekid/', views.mottekinUmsokn, name='mottekid'),
    path('changeProfiles/', views.changeProfiles1, name='changeProfile1'),
    path('changeProfiles2/', views.changeProfiles2, name='changeProfile2'),
    path('changeProfiles3/', views.changeProfiles3, name='changeProfile3')
]
