from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kgf(request):
    return HttpResponse('<marquee><h1>part 3 is pending</h1></marquee>')


def salar(request):
    return HttpResponse('<center><h1>die hard fans</h1></center>')
