from django.shortcuts import render
from . import forms
# Create your views here.
def Registration(request):
    form=forms.StudentRegister();
    return render(request,'testapp1/form1.html',{'form':form})