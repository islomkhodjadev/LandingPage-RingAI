# forms.py

from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "phone", "email", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Name",
                    "required": True,
                    "class": "form-control",
                    "id": "name",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "+998 991234567",
                    "required": True,
                    "class": "form-control",
                    "id": "phone",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email",
                    "required": True,
                    "class": "form-control",
                    "id": "email",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Your message...",
                    "rows": 4,
                    "required": True,
                    "class": "form-control",
                    "id": "message",
                }
            ),
        }
