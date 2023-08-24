from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact-us'),
    path('adult-signup/', views.AdultSignupView.as_view(), name='adult-signup'),
    path('youth-signup/', views.YouthSignupView.as_view(), name='youth-signup'),
]
