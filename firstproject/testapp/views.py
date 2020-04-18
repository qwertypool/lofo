from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_view(request):
    return HttpResponse("<h1>HELLO WORLD</h1>")


def hello1_view(request):
    return HttpResponse("<h2>HELLO WORLD</h2>")


def login_view(request):
    return render(request, 'testapp/login.html')
    

   

