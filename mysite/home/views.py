from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact

def index(request):
    context = {
        "var1": "aman" # key value should be string
    }
    # print("again", datetime.today(), request.method)

    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        contact = Contact(first_name=first_name,last_name=last_name, date=datetime.today())
        contact.save()
    return render(request, "index.html", context)

def about(request):
    return HttpResponse("This is about page.")