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
    

    
