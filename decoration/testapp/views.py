from django.shortcuts import render
from testapp import forms
# Create your views here.
def adhar_view(request):
    form=forms.adharForm
    if request.method=='POST':
        form=forms.adharForm(request.POST)
        if form.is_valid():
            form.save()
        #return return HttpResponseRedirect(reverse('testapp:adhar' ))
    return render(request,'testapp/form.html',{'form':form})
        
