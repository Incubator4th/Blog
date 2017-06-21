from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import RequestContext
from django import forms
# Create your views here.


def index(request):
    return  render(request,'index.html')