from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'task_app/index.html')

def other(request):
    return render(request,'task_app/other.html')
