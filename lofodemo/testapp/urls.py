from django.urls import path
from testapp import views
urlpatterns = [
     path('', views.home_view, name='home'),
     path('about/', views.about_view, name='about'),
     path('lost/', views.lost_view, name='lost'),
     path('found/', views.found_view, name='found'),
     path('logout/', views.logout_view, name='logout'),
     path('signup/', views.signup_view, name='signup'),
     path('notifs/', views.query_view, name='notifs'),


 ]