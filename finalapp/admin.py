from django.contrib import admin
from .models import SingleProduct
from .models import Cartitem,Order,Orderitem

admin.site.register(SingleProduct)
admin.site.register(Cartitem)
admin.site.register(Order)

admin.site.register(Orderitem)




# Register your models here.
