from django.shortcuts import render
from django.views.generic import ListView,DetailView
from testapp.models import Book

# Create your views here.
class BookListView(ListView):
    model=Book 
    #template_name='testapp/custombook.html'

class BookDetailView(DetailView):
    model=Book
