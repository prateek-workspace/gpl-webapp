from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def contactus(request):
    return render(request,"contactus.html")

def registration(request):
    return render(request,"registration.html")