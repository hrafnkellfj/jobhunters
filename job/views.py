from django.shortcuts import render
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