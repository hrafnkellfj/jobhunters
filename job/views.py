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
    title = request.GET.get('title')
    orderby = request.GET.get('orderby')
    if not orderby:
        orderby = "title"

    if not title:
        jobs_return = {'jobs': Job.objects.all().order_by(orderby)}
    else:
        jobs_return = {'jobs': Job.objects.filter(title__icontains=title).order_by(orderby)}

    return render(request, 'job/index.html', jobs_return)

def get_job_by_id(request, id):
    return  render(request, 'job/job_details.html', {
      'job': get_object_or_404(Job, pk=id)
    })


