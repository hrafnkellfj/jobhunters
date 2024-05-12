from django.http import JsonResponse
from django.shortcuts import render , get_object_or_404
from job.models import Job, JobCategory
from datetime import date
from company.models import Company

def index(request):
    job_list = Job.objects.filter(dueDate__gt=date.today())
    categories = JobCategory.objects.all()

    title_query = request.GET.get('title')
    orderby_query = request.GET.get('orderby')
    category_query = request.GET.get('category')
    company_query = request.GET.get('company')
    query_dict = {
        "title": title_query,
        "orderby": orderby_query,
        "category": category_query,
        "company": company_query
    }
    job_list = Job.apply_filters(query_dict, job_list)
    return render(request, 'job/index.html', {'jobs': job_list, 'categories': categories})


def get_job_by_id(request, id):
    return  render(request, 'job/job_details.html', {
      'job': get_object_or_404(Job, pk=id)
    })


