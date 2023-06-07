from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings

from apps.contact.forms import ContactForm
from apps.contact.models import Contact

class ContactView(View):
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                from_email = email
                recipient_list = [settings.EMAIL_HOST_USER]
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

                contact = Contact(name=name, email=email, subject=subject, message=message)
                contact.save()

                messages.success(request, 'Ваш запрос отправлен. Мы скоро к тебе вернемся')
                return redirect('contact')

            except BadHeaderError:
                return HttpResponse('Не отправлено')

    def get(self, request):
        form = ContactForm()
        context = {
            'form': form,
        }
        return render(request, 'pages/contact.html', context)
