from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'main/index.html')
def about(request):
    return render(request,'main/about.html') 
def motor(request):
    return render(request,'main/motor.html')
def motorsmall(request):
    return render(request,'main/motorsmall.html')
