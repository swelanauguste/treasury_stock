from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import (
    DeliveryGoodCreateForm,
    ProductForm,
    ProductUpdateForm,
    ReceiveGoodCreateForm,
    ReceiveGoodUpdateForm,
    SupplierForm,
    SupplierUpdateForm,
    DeliveryGoodUpdateForm,
)
from .models import DeliveryGood, Product, ReceiveGood, Supplier


class DeliveryGoodDetailView(DetailView):
    model = DeliveryGood


class DeliveryGoodListView(ListView):
    model = DeliveryGood


class DeliveryGoodCreateView(SuccessMessageMixin, CreateView):
    model = DeliveryGood
    form_class = DeliveryGoodCreateForm
    success_message = "%(product)s was created successfully"


class DeliveryGoodUpdateView(SuccessMessageMixin, UpdateView):
    model = DeliveryGood
    form_class = DeliveryGoodUpdateForm
    success_message = "%(product)s was updated successfully"


class ReceiveGoodDetailView(DetailView):
    model = ReceiveGood


class ReceiveGoodListView(ListView):
    model = ReceiveGood


class ReceiveGoodCreateView(SuccessMessageMixin, CreateView):
    model = ReceiveGood
    form_class = ReceiveGoodCreateForm
    success_message = "%(product)s was created successfully"


class ReceiveGoodUpdateView(SuccessMessageMixin, UpdateView):
    model = ReceiveGood
    form_class = ReceiveGoodUpdateForm
    success_message = "%(product)s was updated successfully"


class SupplierCreate(SuccessMessageMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    success_message = "%(product)s was created successfully"


class SupplierUpdate(SuccessMessageMixin, UpdateView):
    model = Supplier
    form_class = SupplierUpdateForm
    success_message = "%(product)s was updated successfully"


class SupplierList(ListView):
    model = Supplier


class SupplierDetail(DetailView):
    model = Supplier


class ProductCreate(SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_message = "%(product)s was created successfully"


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


class ProductUpdate(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    success_message = "%(product)s was updated successfully"


class IndexView(TemplateView):
    template_name = "index.html"
