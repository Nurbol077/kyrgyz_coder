from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def batken(request):
    return render(request, 'batken.html')

def osh(request):
    return render(request, 'osh.html')

def jalal_abad(request):
    return render(request, 'jalal_abad.html')

def naryn(request):
    return render(request, 'naryn.html')

def ysyk_kol(request):
    return render(request, 'ysyk_kol.html')

def talas(request):
    return render(request, 'talas.html')

def chuy(request):
    return render(request, 'chuy.html')


def r_batken(request):
    return render(request, 'region_batken/b_raion.html')

def r_chuy(request):
    return render(request, 'region_batken/ch_raion.html')