from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html',{'page':"Home"})


def features(request):
    return render(request,'index.html',{'page':"Fetaures"})

def pricing(request):
    return render(request,'index.html',{'page':"Pricing"})
