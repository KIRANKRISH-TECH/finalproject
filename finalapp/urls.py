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
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.product_list, name='product_list'),
    path('product_list1/', views.product_list1, name='product_list1'),

    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]           


