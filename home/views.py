from django.shortcuts import render


def homepage(request):
    return render(request, "home/index.html")


def aboutpage(request):
    return render(request, "home/about.html")

def getinvolvedpage(request):
    return render(request, "home/involved.html")

def programpage(request):
    return render(request, "home/program.html")