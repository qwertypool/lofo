from django.shortcuts import render
from testapp.forms import NameForm,AgeForm,GfForm
# Create your views here.
def session_view(request):
    count = request.session.get('count',0)
    newcount=count+1
    request.session['count']=newcount
    return render(request,'testapp/session1.html',{'count':newcount})

def name_view(request):
    name=NameForm()
    return render(request,'testapp/name.html',{'name':name})

def age_view(request):
    age=AgeForm()
    name=request.GET['name']
    request.session['name']=name
    return render(request,'testapp/age.html',{'age':age})

def gf_view(request):
    gf=GfForm()
    age=request.GET['age']
    request.session['age']=age
    return render(request,'testapp/gf.html',{'gf':gf})

def result_view(request):
    gf=request.GET['gf']
    request.session['gf']=gf
    return render(request,'testapp/results.html')