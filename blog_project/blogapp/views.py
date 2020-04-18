from django.shortcuts import render,get_object_or_404
from blogapp.models import Post,Comment
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from blogapp.forms import EmailSendForm
from blogapp.forms import CommentForm
from taggit.models import Tag
# Create your views here.

def post_view(request,tag_slug=None):
    post_list_view=Post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list_view=post_list_view.filter(tags__in=[tag])

    paginator=Paginator(post_list_view,2)
    page_number=request.GET.get('page')
    try:
        post_list_view=paginator.page(page_number)
    except PageNotAnInteger:
        post_list_view=paginator.page(1)
    except EmptyPage:
        post_list_view=paginator.page(paginator.num_pages)
    return render(request, 'blogapp/post_list.html', {'post_list_view':post_list_view,'tag':tag})


def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,publish__year=year,publish__month=month,publish__day=day,slug=post)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()
    return render(request,'blogapp/post_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})

def email_view(request,id):
    post=get_object_or_404(Post,id=id)
    sent=False
    if request.method=="POST":
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='{} recommends you to read "{}"'.format(cd['name'],post.title)
            post_url=request.build_absolute_uri(post.get_absolute_url())
            message='Read Post at:\n {} \n \n{}\'s comments:\n{} '.format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'deepapandey364@gmail.com',[cd['to']])
            sent=True
    else:
            form=EmailSendForm()
    return render(request, 'blogapp/email.html', {'form':form,'post':post,'sent':sent})
    

    
    


