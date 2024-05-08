from django.shortcuts import render , get_object_or_404
from job.models import Job, JobCategory
from company.models import Company

def index(request):
    job_list = Job.objects.all()
    categories = JobCategory.objects.all()

    title_query = request.GET.get('title')
    orderby_query = request.GET.get('orderby')
    category_query = request.GET.get('category')
    company_query = request.GET.get('company')
    company = None
    if title_query:
        job_list = job_list.filter(title__icontains=title_query)
    if orderby_query:
        job_list = job_list.order_by(orderby_query)
    if category_query:
        job_list = job_list.filter(category=category_query)
    if company_query:
        company = Company.objects.filter(title__icontains=company_query)
    if company:
        job_list = job_list.filter(company_id=company.id)

    return render(request, 'job/index.html', {'jobs': job_list, 'categories': categories} )

def get_job_by_id(request, id):
    return  render(request, 'job/job_details.html', {
      'job': get_object_or_404(Job, pk=id)
    })


