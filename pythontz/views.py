from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return render(request, 'pythontz/home.html')
