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
    all_jobs = {'jobs': Job.objects.all().order_by('title')}
    return render(request, 'job/index.html', all_jobs)

def get_job_by_id(request, id):
    return  render(request, 'job/job_details.html', {
      'job': get_object_or_404(Job, pk=id)
    })


