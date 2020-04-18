from django.urls import path
from testapp import views

urlpatterns = [
    path('',views.BookListView.as_view(),name='book'),
    path('detail/<int:pk>/',views.BookDetailView.as_view(),name='details'),

    

]