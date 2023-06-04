from django.db import models
from apps.menu.models import Menu
from django.contrib.auth.models import User
import datetime


class Order(models.Model):
    product = models.ForeignKey(Menu,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

    def __str__(self):
        return f"Order #{self.id}"


class CartItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product} - {self.quantity}"
    

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (User: {self.user.username})"