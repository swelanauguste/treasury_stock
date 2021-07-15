from django import forms
from django.forms import widgets

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "date_received": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 3}),
        }
