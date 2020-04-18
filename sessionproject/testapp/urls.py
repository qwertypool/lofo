from django.urls import path
from testapp import views

urlpatterns = [
    path('',views.session_view,name='session'),
    path('n/',views.name_view,name='name'),
    path('a/',views.age_view,name='age'),
    path('g/',views.gf_view,name='gf'),
    path('res/',views.result_view,name='results'),
]