from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from job.models import Job, JobCategory, apply_filters, Application
from datetime import date
from job.forms.post_job import PostJob
from user.models import companyProfile, applicantProfile
from company.models import Company

def index(request):
    """Allows a user to see a list of available jobs."""
    job_list = Job.objects.filter(dueDate__gt=date.today())
    categories = JobCategory.objects.all()

    title_query = request.GET.get('search_title')
    orderby_query = request.GET.get('orderby')
    category_query = request.GET.get('category')
    company_query = request.GET.get('search_company')
    applications = False
    applied_query = False
    user_login = False
    if request.user.is_authenticated:
        try:
            applicant = request.user.applicantprofile.applicant
            applications = Application.objects.filter(applicant=applicant)
            user_login = True
        except applicantProfile.DoesNotExist or TypeError:
            pass #applicant user not logged in
    if user_login:
        applied_query = request.GET.get('applied')
    query_dict = {
        "title": title_query,
        "orderby": orderby_query,
        "category": category_query,
        "company": company_query,
        'applied': applied_query,
        'applications': applications
    }
    job_list = apply_filters(query_dict, job_list)
    if applications:
        applications = {application.job: application.status for application in applications if
                        application.isFinished}
        job_list = {job: applications[job] if job in applications.keys() else {job:False} for job in job_list}
    else:
        job_list = {job:False for job in job_list}
    return render(request, 'job/index.html', {'job_list': job_list, 'categories': categories,
                                              'user_login': user_login})

@login_required
def post_job(request):
    """Allows a company user to make a new job offering"""
    company_profile = companyProfile.objects.get(user=request.user)
    company = company_profile.company
    if request.method == 'POST':
        form = PostJob(data=request.POST)
        if form.is_valid():
            job = Job()
            job.title = form.cleaned_data["title"]
            job.description = form.cleaned_data["description"]
            job.location = form.cleaned_data["location"]
            job.postDate = date.today()
            job.dueDate = form.cleaned_data["dueDate"]
            job.startDate = form.cleaned_data["startDate"]
            job.jobImage = form.cleaned_data["jobImage"]
            job.category = form.cleaned_data["category"]
            job.joBPercentage = form.cleaned_data["jobPercentage"]
            job.company = company
            job.save()
            return redirect('/jobs/job_posted')
        else:
            form = PostJob(data=request.POST)
    else:
        form = PostJob()
    return render(request, 'job/post_job.html', {
        'form': form
    })

def job_posted(request):
    """Delivers a notification to the user that the job posting was successful"""
    return render(request, 'job/job_posted.html')


def get_job_by_id(request, id):
    """Delivers a detailed look at the job with the given id"""
    applicant = False
    application = False
    company = False
    try:
        job = Job.objects.get(pk=id)
    except Job.DoesNotExist:
        raise Http404("Job not found")
    if request.user.is_authenticated:
        try:
            applicant = applicantProfile.objects.get(user=request.user).applicant
        except applicantProfile.DoesNotExist or TypeError:
            pass #user not logged in
        try:
            company = companyProfile.objects.get(user=request.user).company
            company = True
        except companyProfile.DoesNotExist or TypeError:
            pass
        if applicant:
            try:
                application = Application.objects.get(applicant=applicant, job=job)
            except Application.DoesNotExist or TypeError:
                pass #applicant does not have an application
    else:
        applicant = False
        application = False
        company = False

    return render(request, 'job/job_details.html', {
      'job': job, 'applicant': applicant, 'application': application, 'company':company
    })


