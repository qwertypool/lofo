from django.urls import path
from testapp import views
urlpatterns = [
    path('',views.home_view,name='home'),
    path('movie/',views.movies_view,name='movie'),
    path('sport/',views.sports_view,name='sports'),
    path('pol/',views.politics_view,name='politics'),
]
