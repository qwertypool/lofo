from django.urls import path
from testapp import views

urlpatterns = [
    path('form/',views.form_view,name='forms'),
    path('thankyou/',views.thankyou_view,name='thankyou'),
    path('list/',views.list_view,name='list'),
    path('elist/',views.elist_view,name='elist'),
    path('eform/',views.eform_view,name='eform'),
    path('demo/',views.demo_view,name='demo'),

]