from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import forms
from testapp.forms import SignUpForm,adharForm,voterForm,panForm,passportForm,atmForm,FadharForm
from django.http import HttpResponseRedirect
from testapp.models import Fadhar,Adhar
# Create your views here.
def home_view(request):
    return render(request, 'testapp/home.html')
    
@login_required
def about_view(request): 
    return render(request,'testapp/about.html')

@login_required
def lost_view(request): 
    return render(request,'testapp/lost.html')

@login_required
def found_view(request): 
    return render(request,'testapp/found.html')

def logout_view(request):
    return render(request, 'testapp/logout.html')
    
def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'testapp/sign.html', {'form':form})
    
def adhar_view(request):
    form=adharForm()
    if request.method=='POST':
        form=adharForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'testapp/card.html',{'form':form})

def voter_view(request):
    form=voterForm()
    if request.method=='POST':
        form=voterForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'testapp/card.html', {'form':form})
    
def passport_view(request):
    form=passportForm()
    if request.method=='POST':
        form=passportForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'testapp/card.html', {'form':form})

def pan_view(request):
    form=panForm()
    if request.method=='POST':
        form=panForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'testapp/card.html', {'form':form})

def atm_view(request):
    form=atmForm()
    if request.method=='POST':
        form=atmForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'testapp/card.html', {'form':form})

def fadhar_view(request):
    form=FadharForm()
    if request.method=='POST':
        form=FadharForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'testapp/card.html',{'form':form})

    
def thank_view(request):
    return render(request, 'testapp/thankyou.html')
          
def search_view(request):
    q1=Adhar.objects.all().values_list('name','uid')
    q2=Fadhar.objects.all().values_list('name','uid')
    q3=q1.union(q2)
    return render(request,'testapp/search.html',{'q3':q3})

