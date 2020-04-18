from django.shortcuts import render
from testapp.models import FilterModel
# Create your views here.
def filter_view(request):
    filter=FilterModel.objects.all()
    return render(request,'testapp/filter.html',{'filter':filter})