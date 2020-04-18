from django.urls import path
from testapp import views
urlpatterns = [
    path('', views.hellow_world_view.as_view(), name='hello world'),
    path('tem/',views.template_view.as_view(),name='templateview'),
    path('temcon/',views.template_context_view.as_view(),name='template context view'),
]