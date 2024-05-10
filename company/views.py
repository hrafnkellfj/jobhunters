from django.shortcuts import render, get_object_or_404
from company.models import Company
from job.models import Job, Application
from datetime import date
#from django.http import HttpResponse



def index(request):
    all_companies = {'companies': Company.objects.all().order_by('title')}
    return render(request, 'company/index.html', all_companies)

def get_company_by_id(request, id):
    all_company_jobs = Job.objects.filter(company_id=id, dueDate__gt=date.today())
    return render(request, 'company/company_details.html', {
      'company': get_object_or_404(Company, pk=id), 'company_jobs': all_company_jobs
    })

def get_company_job_applications(request, jobid):
    applications = Application.objects.filter(job=jobid)
    if applications:
        job = applications.first().job
        company = applications.first().job.company
        return render(request, 'company/company_job_applications.html', {
            'applications': applications, 'job': job, 'company': company
        })



