from django.urls import path
from . import views
urlpatterns = [
    path('feed/', views.feedback_view,name='feedback'),
    path('thank/', views.thankyou_view,name='thankyou'),
]
