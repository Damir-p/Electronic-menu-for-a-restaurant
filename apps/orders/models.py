from django.db import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User

from apps.menu.models import Menu


class Order(models.Model):
    product = models.ForeignKey(Menu, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()

    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(user=customer_id).order_by('-created_at')

    def __str__(self):
        return f"Order #{self.id}"


class CartItem(models.Model):
    product = models.ForeignKey(Menu, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (User: {self.user.username})"


@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})
