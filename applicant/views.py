from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'applicant/index.html')


def application1(request):
    return render(request, 'applicant/applyToJob_step1.html')


def application2(request):
    return render(request, 'applicant/applyToJob_step2.html')


def application3(request):
    return render(request, 'applicant/applyToJob_step3.html')



def application4(request):
    return render(request, 'applicant/applyToJob_step4.html')



def application5(request):
    return render(request, 'applicant/applyToJob_step5.html')


def mottekinUmsokn(request):
    return render(request, 'applicant/mottekinUmsokn.html')

# Create your views here.
