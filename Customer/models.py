from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.IntegerField(20)
    customer_password = models.CharField(max_length=100) 
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name
