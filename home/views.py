from django.shortcuts import render, redirect

def index(request):
    return render(request, 'home/index.html')

def about_us(request):
    return render(request, 'home/about_us.html')


