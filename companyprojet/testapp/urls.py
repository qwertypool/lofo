from django.urls import path
from testapp import views

urlpatterns = [
    path('list/', views.companylist.as_view(), name='list'),   
    path('details/<int:pk>', views.companydetails.as_view(), name='details'),
    path('form/', views.companycreate.as_view(), name='company'),
    path('update/<int:pk>', views.companyupdate.as_view(), name=''),
    path('delete/<int:pk>', views.companyDelete.as_view(), name='delete'),
]