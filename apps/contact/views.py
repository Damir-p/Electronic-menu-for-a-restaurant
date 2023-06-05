from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings

from apps.contact.forms import ContactForm


class ContactView(View):
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                subject = [subject]
                message = [message]
                from_email = email
                recipient_list = [settings.EMAIL_HOST_USER]
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

                form.save()

                messages.success(request, 'Your inquiry has been submitted. We will get back to you shortly')
                return redirect('contact')

            except BadHeaderError:
                return HttpResponse('Bad Response')

    def get(self, request):
        form = ContactForm()
        context = {
            'form': form,
        }
        return render(request, 'pages/contact.html', context)
