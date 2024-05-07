from django.shortcuts import render
from company.models import Company
#from django.http import HttpResponse



def index(request):
    all_companies = {'companies': Company.objects.all().order_by('title')}
    return render(request, 'company/index.html', all_companies)