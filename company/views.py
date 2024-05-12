from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect

from applicant.forms.change_company_profile import ChangeCompanyProfile
from company.models import Company
from job.models import Job, Application, Recommendation, Experience
from datetime import date
from user.models import companyProfile



def index(request):
    """Gets a list of all companies and sends them to be rendered in html"""
    all_companies = {'companies': Company.objects.all().order_by('title')}
    return render(request, 'company/index.html', all_companies)

def get_company_by_id(request, id):
    """Check a companies profile and all jobs that the company is hiring for"""
    all_company_jobs = Job.objects.filter(company_id=id, dueDate__gt=date.today())
    return render(request, 'company/company_details.html', {
      'company': get_object_or_404(Company, pk=id), 'company_jobs': all_company_jobs
    })

@login_required
def company_job_applications(request, jobid):
    """A company user can, from the profile, see a list of all applications for a job"""
    job = get_object_or_404(Job, pk=jobid)
    company = get_object_or_404(companyProfile, user=request.user).company
    if company and job:
        if job.company == company:
            applications = Application.objects.filter(job=jobid)
            if applications:
                company = applications.first().job.company
                return render(request, 'company/company_job_applications.html', {
                    'applications': applications, 'job': job, 'company': company
                })

    return redirect('/user/profile')

def application_details(request, jobid, appid):
    """A company user can see detailed information about this application"""
    job = get_object_or_404(Job, pk=jobid)
    application = Application.objects.filter(pk=appid).first()
    applicant = application.applicant
    recommendations = Recommendation.objects.filter(applicant=applicant, job=job)
    experiences = Experience.objects.filter(applicant=applicant, job=job)

    return render(request, 'company/application_details.html', {
        'application': application, 'applicant': applicant, 'recommendations':recommendations, 'experiences': experiences
    })




def change_company_profiles(request):
    company = get_object_or_404(Company, id=request.user.id)
    form = ChangeCompanyProfile(instance=company, data=request.POST if request.method == 'POST' else None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('user-profile')
    return render(request, 'company/change_company_profile.html', {
        'form': form
    })













