from django.shortcuts import render
from testapp import forms
# Create your views here.

def student_view(request):
    form=forms.StudentForm
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
            print('DATA INSERTED SUCCESSFULLY !!!!')
    return render(request,'testapp/res1.html',{'form':form})