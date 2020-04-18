from django.urls import path
from testapp import views

urlpatterns = [
    path('base/',views.base_view,name='base'),
    path('index/', views.employee_view, name='employee'),
    path('create/', views.create_view, name='create'),
    path('delete/<int:pk>', views.delete_view, name='delete'),
    path('update/<int:pk>', views.update_view, name='update'),
    path('companyindex/', views.company_view, name='company'),
    path('companycreate/', views.companycreate_view, name='companycreate'),
    path('companyupdate/<int:pk>', views.companyupdate_view, name='companyupdate'),
    path('companydelete/<int:pk>', views.companydelete_view, name='deletecompany'),
    path('orm/', views.orm_view, name='orm'),

]