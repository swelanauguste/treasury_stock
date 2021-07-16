from django.urls import path

from . import views

app_name = "stores"

urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path("", views.ProductList.as_view(), name="product-list"),
    path("create", views.ProductCreate.as_view(), name="product-create"),
    path("detail/<int:pk>", views.ProductDetail.as_view(), name="product-detail"),
    path("update/<int:pk>", views.ProductUpdate.as_view(), name="product-update"),
    # ==============
    path("", views.SupplierList.as_view(), name="supplier-list"),
    path("supplier/create", views.SupplierCreate.as_view(), name="supplier-create"),
    path("supplier/detail/<int:pk>", views.SupplierDetail.as_view(), name="supplier-detail"),
    path("supplier/update/<int:pk>", views.SupplierUpdate.as_view(), name="supplier-update"),
]
