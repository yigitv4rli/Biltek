from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"homepage.html")

def about(request):
    return render(request,"about.html")

def bilim(request):
    return render(request,"bilim.html")

def teknoloji(request):
    return render(request,"teknoloji.html")

def biltek_nostalji(request,):
    return render(request,"bilteknostalji.html")

def all(request):
    return render(request,"all.html")
