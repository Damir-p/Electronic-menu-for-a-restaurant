"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.users.views import SignUpUserView, SignInUserView, LogoutUserView
from apps.orders.views import AddToCartView, CartView, CheckoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.menu.urls')),
    path('blog/', include('apps.blog.urls')),
    path('contact/', include('apps.contact.urls')),
    
    path('signup/', SignUpUserView.as_view(), name='signup'),
    path('login/', SignInUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('cart/', include('apps.orders.urls')),

    path('add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)