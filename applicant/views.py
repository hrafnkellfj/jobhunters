from django.shortcuts import render
from django.http import HttpResponse
from templates.applicant.forms.step1_form import StepOneCreateForm
from templates.applicant.forms.step2_form import StepTwoCreateForm
from templates.applicant.forms.step3_form import StepThreeCreateForm
from templates.applicant.forms.step4_form import StepFourCreateForm
from applicant.models import Applicant


def index(request):
    all_applicants = {'applicants': Applicant.objects.all().order_by('name')}
    return render(request, 'applicant/index.html', all_applicants)

def application1(request):
    if request.method == 'POST':
        form = StepOneCreateForm(data=request.POST)
        if form.is_valid():
            application = form.save()
    else:
        form = StepOneCreateForm()
    return render(request, 'applicant/applyToJob_step1.html', {
        'form': form
    })


def application2(request):
    if request.method == 'POST':
        form = StepTwoCreateForm(data=request.POST)
        if form.is_valid():
            application = form.save()
    else:
        form = StepTwoCreateForm()
    return render(request, 'applicant/applyToJob_step2.html', {
        'form': form
    })


def application3(request):
    if request.method == 'POST':
        form = StepThreeCreateForm(data=request.POST)
        if form.is_valid():
            application = form.save()
    else:
        form = StepThreeCreateForm()
    return render(request, 'applicant/applyToJob_step3.html', {
        'form': form
    })



def application4(request):
    if request.method == 'POST':
        form = StepFourCreateForm(data=request.POST)
        if form.is_valid():
            application = form.save()
    else:
        form = StepFourCreateForm()
    return render(request, 'applicant/applyToJob_step4.html', {
        'form': form
    })

def yfirfara(request):
    if request.method == 'POST':
        form = StepFiveCreateForm(data=request.POST)
        if form.is_valid():
            application = form.save()
    else:
        form = StepFiveCreateForm()
    return render(request, 'applicant/yfirfara.html.html', {
        'form': form
    })


def mottekinUmsokn(request):
    return render(request, 'applicant/mottekinUmsokn.html')


