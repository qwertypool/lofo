from django.urls import path
from . import views
urlpatterns = [
    path('e/', views.Emp_view,name='employee'),
    path('home/',views.index_view,name='index'),
]
