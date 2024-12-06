from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello welcome to home page of this project")
    return render(request,'index.html')
def about(request):
    # return HttpResponse("hello welcome to About page of this project")
    return render(request,'about.html')
def contact(request):
    return HttpResponse("hello welcome to Contact page of this project")