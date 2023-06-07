from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView

from apps.menu.models import Feature, Testimonial, Newsletter, Category, Menu
from apps.menu.models import Category, Menu
from apps.menu.forms import BookingForm
from apps.menu.models import Testimonial



class MenuListView(View):
    def get(self, request):
        categories = Category.objects.all()
        selected_category_id = request.GET.get('category')

        cart = request.session.get('cart', {})
        total_items = sum(cart.values())

        if selected_category_id:
            menu_items = Menu.objects.filter(category_id=selected_category_id)
        else:
            menu_items = Menu.objects.all()

        context = {
            'categories': categories,
            'menu_items': menu_items,
            'selected_category_id': selected_category_id,
            'cart': cart,
            'total_items': total_items,
        }
        return render(request, 'pages/menu.html', context)


class BookingView(View):
    def get(self, request):
        booking_form = BookingForm()
        context = {
            'booking_form': booking_form,
        }
        return render(request, 'pages/booking.html', context)

    def post(self, request):
        booking_form = BookingForm(request.POST)

        if booking_form.is_valid():
            booking_form.save()
            messages.success(request, 'Столик забронирован!')
            return redirect("menu_list")

        context = {
            'booking_form': booking_form,
        }
        return render(request, 'pages/booking.html', context)


class HomeView(View):
    def get(self, request):
        features = Feature.objects.all()
        testimonials = Testimonial.objects.all()
        categories = Category.objects.all()
        context = {
            'features': features,
            'testimonials': testimonials,
            'categories': categories,
        }
        return render(request, 'pages/home.html', context)


class NewsletterView(View):
    def post(self, request):
        email = request.POST['email']

        newsletter = Newsletter(email=email)

        subject = 'Подписка на новости'
        message = 'Привет читатель! Благодарим вас за подписку на еженедельную рассылку новостей Наш Ресторан.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        newsletter.save()
        messages.success(request, 'Благодарим вас за подписку на еженедельный информационный сайт наш Ресторан. Проверьте свой почтовый ящик для получения дополнительной информации')
        return redirect('home')

    def get(self, request):
        return render(request, 'pages/home.html')
    

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        testimonials = Testimonial.objects.all()
        context['testimonials'] = testimonials
        return context
