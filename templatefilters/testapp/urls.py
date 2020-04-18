from django.urls import path
from testapp import views
urlpatterns = [
   path('',views.filter_view,name='filter') 
]