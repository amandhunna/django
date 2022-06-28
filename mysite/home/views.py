from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        "var1": "aman" # key value should be string
    }
    return render(request, "index.html", context)

def about(request):
    return HttpResponse("This is about page.")