from django.db import models





class contacte(models.Model):
    fullname = models.CharField(max_length=100) 
    emailaddress= models.EmailField()
    message = models.TextField()

    def __str__(self):
       
        return self.fullname
    




    from django.db import models

class SingleProduct(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.title

class Cartitem(models.Model):
    product = models.ForeignKey(SingleProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"  


 
class Order(models.Model):
     user = models.CharField(max_length=100)
     order_date = models.DateTimeField(auto_now_add=True)
     total_price = models.DecimalField(max_digits=10, decimal_places=2)
     total_quantity = models.PositiveIntegerField()
     Delivery_address = models.CharField(max_length=255)
     status = models.CharField(max_length=50)
     def __str__(self):
          return f"Order {self.id} by {self.status}"
            
class Orderitem(models.Model):
    order= models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(SingleProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def total(self):
                return self.quantity * self.price
    def __str__(self):
                    return f"{self.productname}  {self.quantity}"
from django.contrib.auth.models import User
              
class Billing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
                

                
          
   

    
