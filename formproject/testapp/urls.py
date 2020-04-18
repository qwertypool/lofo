
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Registration,name='Form'),
]