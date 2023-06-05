from django.urls import path

from apps.menu.views import MenuListView, BookingView, NewsletterView, HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('menu/', MenuListView.as_view(), name='menu_list'),
    path('newsletter/', NewsletterView.as_view(), name='newsletter'),
]
