from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='company_index'),
    path('<int:id>', views.get_company_by_id, name="company_details"),
    path('applications/<int:jobid>', views.company_job_applications, name="company_job_applications"),
    path('applications/<int:jobid>/applicant/<int:appid>', views.application_details, name="application_details"),
    path('changeCompanyProfile/', views.change_company_profile, name='ChangeCompanyProfile'),
]