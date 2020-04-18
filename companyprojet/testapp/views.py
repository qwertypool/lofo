from django.shortcuts import render
from django.urls import reverse_lazy
from testapp.models import Company
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
    
class companylist(ListView):
    model=Company

class companydetails(DetailView):
    model=Company

class companycreate(CreateView):
    model=Company
    fields=('name','location','ceo')

class companyupdate(UpdateView):
    model=Company
    fields=('name','ceo')

class companyDelete(DeleteView):
    model = Company
    success_url = reverse_lazy('list')



