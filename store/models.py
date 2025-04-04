from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Product(models.Model): 
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='uploads/products/', null=True, blank=True)
    is_sale = models.BooleanField(default=False)   
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    
    def __str__(self):
        return self.name

    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=200,default='',blank=True)
    phone = models.CharField(max_length=200,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.product.name}"
    
    
