from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='register'), 
    path('login_view/', views.login_view, name='login_view'),    
    path('index/', views.index, name='index'),
    path('men/', views.men, name='men'),  
    path('women/', views.women, name='women'),
    path('kids/', views.kids, name='kids'),
    path('shoes/', views.shoes, name='shoes'),   
    path('contact/', views.contact, name='contact'),
               
]