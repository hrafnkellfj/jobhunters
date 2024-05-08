from django.shortcuts import render , get_object_or_404
from job.models import Job

#jobs = [
 #   {'title': 'Meindýraeyðir', 'location': 'Reykjavík'},
  #  {'title': 'Nuddari', 'location': 'Eskifjörður'}]
    #serverdót
    #jid
    #cid
    #catid

#def index(request):
    #return render(request, 'job/index.html', context={'jobs': jobs})

def index(request):
    job_list = Job.objects.all()
    title = request.GET.get('title')
    orderby = request.GET.get('orderby')
    if title:
        job_list = job_list.filter(title__icontains=title)
    if orderby:
        job_list = job_list.order_by(orderby)
    return render(request, 'job/index.html', {'jobs': job_list} )

def get_job_by_id(request, id):
    return  render(request, 'job/job_details.html', {
      'job': get_object_or_404(Job, pk=id)
    })


