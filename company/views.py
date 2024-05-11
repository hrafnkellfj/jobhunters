from django.shortcuts import render, get_object_or_404
from company.models import Company
from job.models import Job, Application, Recommendation, Experience
from datetime import date
#from django.http import HttpResponse



def index(request):
    """"""
    all_companies = {'companies': Company.objects.all().order_by('title')}
    return render(request, 'company/index.html', all_companies)

def get_company_by_id(request, id):
    """"""
    all_company_jobs = Job.objects.filter(company_id=id, dueDate__gt=date.today())
    return render(request, 'company/company_details.html', {
      'company': get_object_or_404(Company, pk=id), 'company_jobs': all_company_jobs
    })

def company_job_applications(request, jobid):
    """"""
    applications = Application.objects.filter(job=jobid)
    if applications:
        job = applications.first().job
        company = applications.first().job.company

        return render(request, 'company/company_job_applications.html', {
            'applications': applications, 'job': job, 'company': company
        })
    #return error dæmi

def application_details(request, jobid, appid):
    """"""
    application = Application.objects.filter(pk=appid).first()
    applicant = application.applicant
    recommendations = Recommendation.objects.filter(applicant=applicant, applied_job=application)
    experiences = Experience.objects.filter(applicant=applicant, applied_job=application)

    return render(request, 'company/application_details.html', {
        'application': application, 'applicant': applicant, 'recommendations':recommendations, 'experiences': experiences
    })




















