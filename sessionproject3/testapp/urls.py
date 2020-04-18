from django.urls import path
from testapp import views

urlpatterns = [
    path('a/',views.add_view,name='add'),
    path('d/', views.display_view, name='display'),
]