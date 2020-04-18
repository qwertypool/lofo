from django.shortcuts import render,redirect
from testapp.models import Employee,Company
from testapp.forms import EmployeeForm,CompanyForm
# Create your views here.
def base_view(request):
    return render(request, 'testapp/base.html')
    

def employee_view(request):
    employees=Employee.objects.all()
    return render(request, 'testapp/index.html', {'employees':employees})

def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home/index')
    return render(request,'testapp/create.html',{'form':form})

def delete_view(request,pk):
    employee=Employee.objects.get(id=pk)
    employee.delete()
    return redirect('/home/index')
        

def update_view(request,pk):
    employee=Employee.objects.get(id=pk)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/home/index')
    return render(request, 'testapp/update.html', {'employee':employee})
   
def company_view(request):
    company=Company.objects.all()
    return render(request, 'testapp/companyindex.html', {'company':company})

def companycreate_view(request):
    form=CompanyForm()
    if request.method=="POST":
        form=CompanyForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/home/companyindex')
    return render(request, 'testapp/create.html', {'form':form})

def companyupdate_view(request,pk):
    company=Company.objects.get(id=pk)
    if request.method=='POST':
        form=CompanyForm(request.POST,instance=company)
        if form.is_valid():
            form.save()
        return redirect('/home/companyindex')
    return render(request, 'testapp/companyupdate.html', {'company':company})
    
def orm_view(request):
    #q1=Employee.objects.filter(id__in[(Entry.objects.values_list('enum'))])
    q1=Employee.objects.filter(enum__gt=10).values('enum')
    q2=Company.objects.filter(cnum__gt=10).values('cnum')
    #Entry.objects.filter(id__gt=4)
    #q2=Company.objects.values_list('cnum')
    q3=q1.intersection(q2)
    print (q1.query)
    return render(request, 'testapp/orm.html', {'q3':q3})
    

def companydelete_view(request,pk):
    company=Company.objects.get(id=pk)
    company.delete()
    return redirect('/home/companyindex')

    
    
          