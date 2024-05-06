from django.shortcuts import render
from django.http import HttpResponse

jobs = [
    {'title': 'Meindýraeyðir', 'location': 'Reykjavík'},
    {'title': 'Nuddari', 'location': 'Eskifjörður'}]
    #serverdót
    #jid
    #cid
    #catid

def index(request):
    return render(request, 'job/index.html', context={'jobs': jobs})

