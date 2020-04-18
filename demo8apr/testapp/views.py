from django.shortcuts import render
from testapp.models import Myself,Enemies,Demo
from testapp.forms import MyselfForm,EnemiesForm,DemoForm
# Create your views here.
#  def form_view(request):
#    form=forms.MyselfForm
#    if request.Method=='POST':
#        form=forms.MyselfForm(request.post)
#        if form.is_valid():
#            form.save()
#         return render(request,'testapp/form.html',{'form':form})

def form_view(request):
    form=MyselfForm()
    if request.method=='POST':
        form=MyselfForm(request.POST)
        if form.is_valid():
            form.save()
        return thankyou_view(request)
    return render(request, 'testapp/form.html', {'form':form})
    

def thankyou_view(request):
    return render(request,'testapp/thankyou.html')

def list_view(request):
    list=Myself.objects.all().order_by('age')
    return render(request, 'testapp/list.html', {'list':list})

def eform_view(request):
    eform=EnemiesForm()
    if request.method=='POST':
        eform=EnemiesForm(request.POST)
        if eform.is_valid():
            eform.save()
        return thankyou_view(request)
    return render(request, 'testapp/form.html', {'eform':eform})
        
def elist_view(request):
    elist=Enemies.objects.all()
    return render(request, 'testapp/elist.html', {'elist':elist})
    
def demo_view(request):
    demo=DemoForm()
    if request.method=='POST':
        demo=DemoForm(request.POST)
        if demo.is_valid():
            demo.save(commit=True)
        return thankyou_view(request)
    return render(request, 'testapp/demo.html', {'demo':demo})

def demolist_view(request):
    list=Demo.objects.all()
    print(list.subject[0])
    

# def add_movie_view(request):
#      10) form=MovieForm() 
#      11) if request.method=='POST': 
#      12) form=MovieForm(request.POST) 
#      13) if form.is_valid(): 
#      14) form.save() 
#      15) return index_view(request) 
#      16) return render(request,'testapp/addmovie.html',{'form':form})