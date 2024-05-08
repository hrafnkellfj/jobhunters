from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'home/index.html')

def about_us(request):
    return render(request, 'home/about_us.html')
def login(request):
    return render(request, 'home/login.html')

def signup(request):
    return render(request, 'home/signup.html')