from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'applicant/index.html')


def application1(request):
    return render(request, 'applicant/applyToJob_step1.html')


def application2(request):
    return render(request, 'applicant/applyToJob_step2.html')

# Create your views here.
