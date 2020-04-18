from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from work.models import Lost,Found
# Create your views here.

def work_view(request):
    return render(request, 'work/random.html')


def lost_view(request):
    if not request.user.is_authenticated:
        return render(request, 'loginredirect.html')
    if request.method=='POST':
        name=request.POST['name']
        uid=request.POST['uid']
        card=request.POST['cardtype']
        details=request.POST['details']
        lostcard=Lost(name=name,uid=uid,card=card,details=details)
        lostcard.save()
        messages.success(request,"Your Card details has been recorded!")
    return render(request, 'work/lostcard.html')
    

def found_view(request):
    if not request.user.is_authenticated:
        return render(request, 'loginredirect.html')
    if request.method=='POST':
        foundername=request.POST['foundername']
        foundname=request.POST['foundname']
        founduid=request.POST['founduid']
        foundcard=request.POST['foundcardtype']
        details=request.POST['founddetails']
        foundcard=Found(name=foundername,cardholder_name=foundname,uid=founduid,card=foundcard,details=details)
        foundcard.save()
        messages.success(request,"Your Card details has been recorded!")
    return render(request, 'work/foundcard.html')





def notification_view(request):
     #q1=Found.objects.values_list('uid','card')
    q1=Found.objects.filter(uid__gt=1).values('uid','card','cardholder_name')
    q2=Lost.objects.filter(uid__gt=1).values('uid','card','name')
    q4=Found.objects.values('uid')
    #q2=Lost.objects.values_list('uid','card',flat=True)
    print(q1.query)
    print(q2.query)
    q3=q1.intersection(q2)
    x=[]
    for q in q3:
        x=q['uid']
    fname=Found.objects.filter(uid__exact=x).values('name')
    #founder_name=Found.objects.filter(q3.uid__iexact=q4)
    return render(request,'work/notifications.html',{'q3':q3,'fname':fname})
    #q2=Found.objects.
    #Entry.objects.values_list('id', 'headline', named=True)




    # # course_qs = <whatever query gave you the queryset>
    # # for course in course_qs:
    # #     print(course['course_code']










    # if not request.user.is_authenticated:
#         return render(request, 'loginredirect.html')
        
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         content = request.POST['content']
#         if len(name) < 2 or len(phone) < 10 or len(content) < 2:
#             messages.error(request, "Please fill the form correctly!")
#         else:
#             contact = Contact(name=name, email=email,
#                               phone=phone, content=content)
#             contact.save()
#             messages.success(request, "Your Query has been sent!")
#     return render(request, 'home/contact.html')


# @login_required
# def lost_view(request):
#     form=LostForm()
#     if request.method=="POST":
#         form=LostForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return HttpResponseRedirect('/home')
#     return render(request, 'testapp/form.html', {'form':form})


# @login_required
# def found_view(request):
#     form=FoundForm()
#     if request.method=="POST":
#         form=FoundForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return HttpResponseRedirect('/home')
#     return render(request, 'testapp/form.html', {'form':form})

# def query_view(request):
#     #q1=Found.objects.values_list('uid','card')
#     q1=Found.objects.filter(uid__gt=1).values('uid','card')
#     q2=Lost.objects.filter(uid__gt=1).values('uid','card')
#     #q2=Lost.objects.values_list('uid','card',flat=True)
#     print(q1.query)
#     print(q2.query)
#     q3=q1.intersection(q2)
#     return render(request,'testapp/notifications.html',{'q3':q3})
#     #q2=Found.objects.
#     #Entry.objects.values_list('id', 'headline', named=True)

# #def notifications_view(request):
#  #   return render(request, 'testapp/notifications.html', {})