from django.shortcuts import render
from django.views import View
from orders.models import Order

class OrderView(View):
    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request , 'cart.html'  , {'orders' : orders})