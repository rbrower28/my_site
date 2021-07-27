from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound


# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def post(request, slug):
    return render(request, "blog/post-detail.html")