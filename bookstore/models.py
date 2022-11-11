from django.db import models


    
class Customer(models.Model):
    
    TYPE_CHOICES = [
        ('G', 'Gold'),
        ('R', 'Regular'),
    ]
    
    id = models.PositiveIntegerField(primary_key=True, null=False, db_index=True)
    name = models.CharField(max_length=20, null=False)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='R')
    email_id = models.EmailField(null=False)
    address = models.CharField(max_length=50, null=False)
    
    
    def __str__(self) -> str:
        return self.name
    
    
class GoldCustomer(Customer):
    date_joined = models.DateField(null=False)
    coupon =  models.CharField(max_length=10)


class StoreItem(models.Model):
    item_id = models.PositiveIntegerField(primary_key=True, null=False, db_index=True)
    price = models.FloatField(range(0, 1000))
    copies = models.PositiveIntegerField(default=0)
    
    def __str__(self) -> str:
        return str(self.item_id)
    

class CartoonMovie(StoreItem):
    title = models.CharField(max_length=20)
    studio_name = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    
    def __str__(self) -> str:
        return self.title
    
    
class ComicBook(StoreItem):
    title = models.CharField(max_length=20)
    published_date = models.DateField(null=True)
    
    def __str__(self) -> str:
        return self.title


class OrderLineItem(models.Model):
    line_id = models.PositiveIntegerField(primary_key=True, null=False, db_index=True)
    store_item = models.ForeignKey(StoreItem, on_delete=models.CASCADE, null=False)
    quantity = models.PositiveIntegerField(default=0)
    

class Order(models.Model):
    id = models.PositiveIntegerField(primary_key=True, db_index=True)
    cust_id = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    order_line_item = models.ForeignKey(OrderLineItem, null=False, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    shipping_date = models.DateField(default=None, blank=True, null=True)
    shipping_fee = models.FloatField(default=None, blank=True, null=True)