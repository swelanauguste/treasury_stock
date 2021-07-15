from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    CreateView,
    UpdateView,
)

from .forms import ProductForm

from .models import Product


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


class ProductUpdate(UpdateView):
    model = Product
    fields = "__all__"


class IndexView(TemplateView):
    template_name = "index.html"
