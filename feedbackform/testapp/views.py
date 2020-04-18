from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
# Create your views here.
def thankyou_view(request):
    return render(request,'testapp/thankyou.html')

def feedback_view(request):
    form=forms.FeedbackForm()
    if request.method=='POST':
        form=forms.FeedbackForm(request.POST)
        if form.is_valid():
            print('FORM VALIDATION SUCCESS AND PRINTING FEEDBACK INFO::')
            print('STUDENT NAME:',form.cleaned_data['Name'])
            print('STUDENT ROLL NO. :',form.cleaned_data['rollno'])
            print('STUDENT MAIL ID: ',form.cleaned_data['email'])
            print('STUDENT FEEDBACK : ',form.cleaned_data['feedback'])
            return thankyou_view(request)      
    return render(request,'testapp/feedback.html',{'form':form})

    