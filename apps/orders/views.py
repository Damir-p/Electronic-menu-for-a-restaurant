from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from apps.orders.models import Order, CartItem
from apps.menu.models import Menu
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator


class AddToCartView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        product = Menu.objects.get(id=product_id)
        
        cart = request.session.get('cart', {})
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity
        request.session['cart'] = cart
        
        return redirect('menu_list')



@method_decorator(login_required, name='dispatch')
class CartView(TemplateView):
    template_name = 'pages/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=self.request.user)
            context['cart_items'] = cart_items
        else:
            context['cart_items'] = []
        return context


class CheckoutView(View):
    def post(self, request):
        cart = request.session.get('cart', {})
        cart_items = CartItem.objects.filter(id__in=cart.keys())
        
        order = Order.objects.create(user=request.user)  # Предполагается, что пользователь авторизован
        
        for item in cart_items:
            quantity = cart[item.id]
            order.cart_items.create(product=item.product, quantity=quantity)
        
        del request.session['cart']
        
        return redirect('order_confirmation')


class OrderConfirmationView(View):
    def get(self, request):
        order = Order.objects.latest('created_at')
        
        context = {
            'order': order,
        }
        return render(request, 'order.html', context)


class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.objects.filter(user=request.user)
        return render(request, 'orders.html', {'orders': orders})



