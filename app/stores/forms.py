from django import forms
from django.forms import widgets

from .models import Product, Supplier, ReceiveGood, DeliveryGood


class DeliveryGoodCreateForm(forms.ModelForm):
    class Meta:
        model = DeliveryGood
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "delivery_date": forms.DateInput(attrs={"type": "date"}),
            "delivery_comment": forms.Textarea(attrs={"rows": 3}),
        }


class DeliveryGoodUpdateForm(forms.ModelForm):
    class Meta:
        model = DeliveryGood
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "delivery_comment": forms.Textarea(attrs={"rows": 3}),
        }


class ReceiveGoodCreateForm(forms.ModelForm):
    class Meta:
        model = ReceiveGood
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "received_date": forms.DateInput(attrs={"type": "date"}),
            "received_comment": forms.Textarea(attrs={"rows": 3}),
        }


class ReceiveGoodUpdateForm(forms.ModelForm):
    class Meta:
        model = ReceiveGood
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "received_comment": forms.Textarea(attrs={"rows": 3}),
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        exclude = ["created_by", "updated_by"]


class SupplierUpdateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        exclude = ["created_by", "updated_by"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "date_received": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 3}),
        }


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "date_received": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 3}),
        }
