app_name='blogapp'
from django.urls import path
from blogapp.models import Post
from django.views.generic.dates import ArchiveIndexView
from blogapp import views

urlpatterns = [
    path('home/',views.post_view,name='home'),
    path('details/(?P<year>\d{4})/(?P<month>[-\B]+)/(?P<day>\d{2})/(?P<post>[-\w]+)/$',views.post_detail_view,name='post-details'),
    #path('details/<int:year>/<slug:post>/',views.post_detail_view,name='post-details'),
    # path('details/<int:year>/<str:month>/<int:day>/<slug:post>/',views.post_detail_view,name='post-details'),
    #path('details/(?P<year>\d{4})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',views.post_detail_view,name='post-details'),
    #  path('details/<str:month>/<slug:post>/',views.post_detail_view,name='post-details'),
    #path('mail/(?P<id>\d+)/$',views.email_view,name='email'),
    path('mail/<int:id>',views.email_view,name='email'),
    path('tag/<slug:tag_slug>',views.post_view,name='post_list_by_tag_name')
    #path('tag/(?P<tag_slug>[-\w]+)/$',views.post_view,name='post_list_by_tag_name')
]

