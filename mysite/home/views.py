from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse("This is about page.")