from django.shortcuts import render, get_object_or_404
from company.models import Company
from job.models import Job
#from django.http import HttpResponse



def index(request):
    all_companies = {'companies': Company.objects.all().order_by('title')}
    return render(request, 'company/index.html', all_companies)

def get_company_by_id(request, id):
    all_company_jobs = Job.objects.filter(company_id=id)
    valid_company_jobs = [job for job in all_company_jobs if not job.isDue()]
    return render(request, 'company/company_details.html', {
      'company': get_object_or_404(Company, pk=id), 'company_jobs': valid_company_jobs
    })