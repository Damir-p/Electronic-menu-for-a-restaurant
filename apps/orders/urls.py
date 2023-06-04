from django.urls import path
from django.contrib.auth.views import LoginView
# from apps.orders.views import AddToCartView, CartView, CheckoutView


# urlpatterns = [
#     path('add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
#     path('', CartView.as_view(), name='cart'),
#     path('checkout/', CheckoutView.as_view(), name='checkout'),
# ]

urlpatterns = [
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
]
