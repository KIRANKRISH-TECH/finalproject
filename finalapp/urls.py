from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'), 
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
    path('remove_cart_item/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('update_cart_item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    # path('process_order/', views.process_order, name='process_order'),
    path('order_summary/<int:order_id>/', views.order_summary, name='order_summary'),
    path("payment-success/", views.payment_success, name="payment_success"),
    path("order-history/", views.order_history, name="order_history"),
     path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),




  
]           



