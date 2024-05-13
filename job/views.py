from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from job.models import Job, JobCategory, apply_filters, Application
from datetime import date
from job.forms.post_job import PostJob
from user.models import companyProfile, applicantProfile
from company.models import Company

def index(request):
    """"""
    job_list = Job.objects.filter(dueDate__gt=date.today())
    categories = JobCategory.objects.all()

    title_query = request.GET.get('title')
    orderby_query = request.GET.get('orderby')
    category_query = request.GET.get('category')
    company_query = request.GET.get('company')
    applied_query = request.GET.get('applied')
    applicant = False
    applications = False
    if request.user:
        applicant = get_object_or_404(applicantProfile).applicant
        if applicant:
            applications = Application.objects.filter(applicant=applicant)
            applications = {application.job_id: application.status for application in applications}
    query_dict = {
        "title": title_query,
        "orderby": orderby_query,
        "category": category_query,
        "company": company_query,
        'applied': applied_query,
        'applicant': applicant
    }
    job_list = apply_filters(query_dict, job_list)
    if applications:
        job_list = {job: applications[job.id] if job.id in applications else {job:False} for job in job_list}
    return render(request, 'job/index.html', {'jobs': job_list, 'categories': categories})

def post_job(request):
    company_profile = companyProfile.objects.get(user=request.user)
    company = company_profile.company
    if request.method == 'POST':
        form = PostJob(data=request.POST)
        if form.is_valid():
            job = form.save(commit=False)  # Do not save the form yet, need to add extra fields
            job.jobPercentage = form.cleaned_data['jobPercentage']
            job.dueDate = form.cleaned_data['dueDate']
            job.startDate = form.cleaned_data['startDate']
            job.postDate = date.today()  # Use Django's timezone now
            job.company = company  # Access company ID from session
            job.save()  # Now save the job with all fields properly assigned
            return redirect('/jobs/job_posted')
        else:
            form = PostJob()
    else:
        form = PostJob()
    return render(request, 'job/post_job.html', {
        'form': form
    })

def job_posted(request):
    return render(request, 'job/job_posted.html')

def get_job_by_id(request, id):
    return  render(request, 'job/job_details.html', {
      'job': get_object_or_404(Job, pk=id)
    })


