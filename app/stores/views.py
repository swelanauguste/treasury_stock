from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    CreateView,
    UpdateView,
)

from .forms import ProductForm, ProductUpdateForm, SupplierForm, SupplierUpdateForm

from .models import Product, Supplier


class SupplierCreate(CreateView):
    model = Supplier
    form_class = SupplierForm


class SupplierUpdate(UpdateView):
    model = Supplier
    form_class = SupplierUpdateForm


class SupplierList(ListView):
    model = Supplier


class SupplierDetail(DetailView):
    model = Supplier


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductUpdateForm


class IndexView(TemplateView):
    template_name = "index.html"
