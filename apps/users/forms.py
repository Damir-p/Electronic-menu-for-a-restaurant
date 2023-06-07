from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control text-bg-dark",
        "aria-label": "Password",
        "aria-describedby": "inputGroup-sizing-default",
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control text-bg-dark",
        "aria-label": "Confirm password",
        "aria-describedby": "inputGroup-sizing-default",
    }))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password", "confirm_password"]
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "First name"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "Last name",
            }),
            "username": forms.TextInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "Username",
                "aria-describedby": "addon-wrapping",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "E-mail",
                "aria-describedby": "inputGroup-sizing-default",
            }),
        }
