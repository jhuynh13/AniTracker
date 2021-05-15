from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>In Index</>")

def home(response):
    return HttpResponse("<h1>In Home</>")

def library(response):
    return HttpResponse("<h1>In LIbrary</>")