from django.shortcuts import render
from django.views.generic import TemplateView,View
from django.http import HttpResponse
# Create your views here.

class hellow_world_view(View):
    def get(self,request):
        return HttpResponse('<h1>hello world</h1>')

class template_view(TemplateView):
    template_name='testapp/tem.html'

class template_context_view(TemplateView):
    template_name='testapp/temcon.html'
    def get_context_data(self, **kwargs):
        context = super(template_context_view, self).get_context_data(**kwargs)
        context['name']='DEEPA'
        context['city']='kolkata'
        context['college']='gcetts'
        return context
    