from django.shortcuts import render
from testapp.models import employee
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def Emp_view(request):
    emp_list=employee.objects.all()
    return render(request,'testapp/res1.html',{'emp_list':emp_list})

def index_view(request):
    return render(request,'testapp/index.html')