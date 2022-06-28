# from django.shortcuts import render, HttpResponse

# # Create your views here.
# def index(request):
#     return HttpResponse("this is home page")

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")