from django.db import models

class Customer(models.Model):
  customer_name = models.CharField(max_length=255)
  address = models.CharField(max_length=255, default=None)
  phone = models.CharField(max_length=255, default=None)
  
  def __str__(self):
    return self.customer_name

class Product(models.Model):
  item_code = models.CharField(max_length=45)
  item_name = models.CharField(max_length=255)
  price = models.FloatField(default=None)
  tin_size = models.CharField(max_length=10, default=None)
  def __str__(self):
    return self.item_code

class Stock(models.Model):
  product_id = models.IntegerField()
  quantity = models.IntegerField()
  updated_at = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f"{self.product_id} {self.quantity}"

class Supplier(models.Model):
  customer_name = models.CharField(max_length=255)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.customer_name


class Order(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  status = models.IntegerField(choices=((1,"processed"),(0,"not processed")), default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  processed_at = models.DateTimeField(default=None)
  def __str__(self):
    return f"{self.product} {self.quantity}"