from django.db import models


class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)



class contact(models.Model):
    email = models.EmailField()
    message = models.TextField()



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
   

    
