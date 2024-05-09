from django.shortcuts import render
from django.http import HttpResponse
from templates.applicant.forms.step1_application_form import StepOneCreateForm
from templates.applicant.forms.step1_changep_form import StepOneChangeProfile
from templates.applicant.forms.step2_application_form import StepTwoCreateForm
from templates.applicant.forms.step3_application_form import StepThreeCreateForm
from templates.applicant.forms.step4_application_form import StepFourCreateForm


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


def changeProfiles1(request):
    if request.method == 'POST':
        print(1)
    else:
        form = StepOneChangeProfile()
    return render(request, 'applicant/changeProfile_step1.html', {
        'form': form
    })


def changeProfiles2(request):
    ...


def changeProfiles3(request):
    ...


def changeProfiles4(request):
    ...

# Create your views here.
