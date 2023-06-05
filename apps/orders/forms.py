from django import forms


class OrderForm(forms.Form):
    quantity = forms.IntegerField(label='Количество')


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(label='Количество')
