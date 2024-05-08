from django.shortcuts import render
from django.http import HttpResponse
from templates.applicant.forms.step1_form import StepOneCreateForm
from templates.applicant.forms.step2_form import StepTwoCreateForm
from templates.applicant.forms.step3_form import StepThreeCreateForm
from templates.applicant.forms.step4_form import StepFourCreateForm


def index(request):
    return render(request, 'applicant/index.html')


def application1(request):
    if request.method == 'POST':
        print(1)
    else:
        form = StepOneCreateForm()
    return render(request, 'applicant/applyToJob_step1.html', {
        'form': form
    })


def application2(request):
    if request.method == 'POST':
        print(1)
    else:
        form = StepTwoCreateForm()
    return render(request, 'applicant/applyToJob_step2.html', {
        'form': form
    })


def application3(request):
    if request.method == 'POST':
        print(1)
    else:
        form = StepThreeCreateForm()
    return render(request, 'applicant/applyToJob_step3.html', {
        'form': form
    })



def application4(request):
    if request.method == 'POST':
        print(1)
    else:
        form = StepFourCreateForm()
    return render(request, 'applicant/applyToJob_step4.html', {
        'form': form
    })



def yfirfara(request):
    return render(request, 'applicant/yfirfara.html')


def mottekinUmsokn(request):
    return render(request, 'applicant/mottekinUmsokn.html')

# Create your views here.
