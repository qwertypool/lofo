from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from testapp.models import Lost,Found
from testapp.forms import LostForm,FoundForm,SignUpForm
# Create your views here.
def home_view(request):
    return render(request, 'testapp/home.html',{})

@login_required
def lost_view(request):
    form=LostForm()
    if request.method=="POST":
        form=LostForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/home')
    return render(request, 'testapp/form.html', {'form':form})

@login_required
def found_view(request):
    form=FoundForm()
    if request.method=="POST":
        form=FoundForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/home')
    return render(request, 'testapp/form.html', {'form':form})


def logout_view(request):
    return render(request, 'testapp/logout.html')

@login_required
def about_view(request):
    return render(request, 'testapp/about.html')

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'testapp/signup.html', {'form':form})

def query_view(request):
    #q1=Found.objects.values_list('uid','card')
    q1=Found.objects.filter(uid__gt=1).values('uid','card')
    q2=Lost.objects.filter(uid__gt=1).values('uid','card')
    #q2=Lost.objects.values_list('uid','card',flat=True)
    print(q1.query)
    print(q2.query)
    q3=q1.intersection(q2)
    return render(request,'testapp/notifications.html',{'q3':q3})
    #q2=Found.objects.
    #Entry.objects.values_list('id', 'headline', named=True)

#def notifications_view(request):
 #   return render(request, 'testapp/notifications.html', {})
    