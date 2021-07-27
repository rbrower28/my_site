from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

# Create your views here.

def index(request):
    return HttpResponse("<h1>What's up world!</h1>")

def posts(request):
    pass

def first_post(request):
    pass