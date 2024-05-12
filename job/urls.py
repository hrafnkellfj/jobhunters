from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.get_job_by_id, name="job_details"),
    path('post_job', views.post_job, name='post-job'),
    path('job_posted', views.job_posted, name='job-posted')

]
