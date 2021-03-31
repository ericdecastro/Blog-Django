from django.http import HttpResponse
from django.shortcuts import render


def about_func(request):
    return render(request, "about.html")
