from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        widgets = {
            "first_name": TextInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "First name"
            }),
            "last_name": TextInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "Last name",
            }),
            "username": TextInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "Username",
                "aria-describedby": "addon-wrapping",
            }),
            "email": EmailInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "E-mail",
                "aria-describedby": "inputGroup-sizing-default",
            }),
            "password": PasswordInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "Password",
                "aria-describedby": "inputGroup-sizing-default",
            }),
        }
    