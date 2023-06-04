from django.test import TestCase, Client
from django.urls import reverse
from apps.menu.models import Booking
from apps.menu.forms import BookingForm


class MenuListViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_menu_list_view(self):
        url = reverse('menu_list')  
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/menu.html')


class BookingViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('booking') 

    def test_booking_view_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/booking.html')
        self.assertIsInstance(response.context['booking_form'], BookingForm)

    def test_booking_view_post_valid_form(self):
        form_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'mobile': '1234567890',
            'date': '2022-01-01',
            'time': '12:00',
            'no_of_persons': 4,
        }
        response = self.client.post(self.url, form_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/booking.html')
        self.assertIsInstance(response.context['booking_form'], BookingForm)
        self.assertTrue(response.context['booking_form'].is_valid())
        self.assertEqual(Booking.objects.count(), 1)

    def test_booking_view_post_invalid_form(self):
        form_data = {
            'name': '',
            'email': 'johndoe@example.com',
            'mobile': '1234567890',
            'date': '2022-01-01',
            'time': '12:00',
            'no_of_persons': 4,
        }
        response = self.client.post(self.url, form_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/booking.html')
        self.assertIsInstance(response.context['booking_form'], BookingForm)
        self.assertFalse(response.context['booking_form'].is_valid())
        self.assertEqual(Booking.objects.count(), 0)