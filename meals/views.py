from django.shortcuts import render, redirect
from . models import Feature, Testimonial, Newsletter
from menu.models import Category
from django.contrib import messages
from django.core.mail import send_mail
from main import settings


# Create your views here.


def home(request):
    features = Feature.objects.all()
    testimonials = Testimonial.objects.all()
    categories = Category.objects.all()
    context = {
        'features': features,
        'testimonials': testimonials,
        'categories': categories,
    }

    return render(request, 'pages/home.html', context)


def newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']

        newsletter = Newsletter(email=email)

        #  Email
        subject = 'Подписка на новости'
        message = 'Привет читатель! Благодарим вас за подписку на еженедельную рассылку новостей Наш Ресторан.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email,
                  recipient_list, fail_silently=False)

        newsletter.save()
        messages.success(
            request, 'Благодарим вас за подписку на еженедельный информационный бюллетень \Наш Ресторан\. Проверьте свой почтовый ящик для получения дополнительной информации')
        redirect('home')

    return render(request, 'pages/home.html')
