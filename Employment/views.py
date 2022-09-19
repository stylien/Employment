import imp
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")
def page2(request):
    return render(request,"page2.html")
def landlord(request):
    return render(request,"landlord.html")
def labour(request):
    return render(request,"labour.html")
def final(request):
    return render(request,"final.txt")