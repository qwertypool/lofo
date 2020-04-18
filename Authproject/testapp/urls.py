from django.urls import path
from testapp import views

urlpatterns = [
    path('',views.home_view, name='home'),
    path('about/',views.about_view, name='about'),
    path('lost/',views.lost_view, name='lost'),
    path('found/',views.found_view, name='found'),
    path('logout/',views.logout_view, name='logout'),
    path('sign/',views.signup_view, name='signup'),
    path('adhar/', views.adhar_view, name='adhar_card'),
    path('voter/', views.voter_view, name='voter_card'),
    path('passport/', views.passport_view, name='passport_card'),
    path('pan/', views.pan_view, name='pan_card'),
    path('atm/', views.atm_view, name='atm_card'),
    path('fadhar/', views.fadhar_view, name='fadhar_card'),
    path('thank/', views.thank_view, name='thankyou'),
    path('search/', views.search_view, name='search'),

]

