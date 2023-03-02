from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello, World! this is my first python webpage")
    return render(request, 'details.html')

def about(request):
    return HttpResponse("About page")

def contact(request):
    return HttpResponse("Contact page")
