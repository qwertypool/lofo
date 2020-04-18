from django.shortcuts import render

# Create your views here.
def count_view(request):
    count=int(request.COOKIES.get('count',0))
    newcount=count+1
    response=render(request,'testapp/count.html',{'count':newcount})
    response.set_cookie('count',newcount)
    return response

def name_view(request):
    return render(request,'testapp/name.html')

def age_view(request):
    name=request.GET['name']
    response=render(request,'testapp/age.html')
    response.set_cookie('name',name)
    return response

def gf_view(request):
    age=request.GET['age']
    response=render(request,'testapp/gf.html')
    response.set_cookie('age',age)
    return response

def result_view(request):
    gf=request.GET['gf']
    name=request.COOKIES.get('name')
    age=request.COOKIES.get('age')
    return render(request,'testapp/results.html',{'name':name,'age':age,'gf':gf})