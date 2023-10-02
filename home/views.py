from django.shortcuts import render

# Create your views here.

def parent(request):
    return render(request,"parent.html")

def login(request):
    return render(request,"login.html")

def index(request):
    return render(request,"index.html")