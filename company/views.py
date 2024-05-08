from django.shortcuts import render, get_object_or_404
from company.models import Company
#from django.http import HttpResponse



def index(request):
    all_companies = {'companies': Company.objects.all().order_by('title')}
    return render(request, 'company/index.html', all_companies)

def get_company_by_id(request, id):
    return  render(request, 'company/company_details.html', {
      'company': get_object_or_404(Company, pk=id)
    })