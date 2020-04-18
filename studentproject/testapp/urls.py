
from django.urls import path
from testapp import views

urlpatterns = [
    path('',views.student_view,name='studentform'),
]
