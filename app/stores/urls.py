from django.urls import path

from . import views

app_name = "stores"

urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path("", views.ProductList.as_view(), name="list"),
    path("create", views.ProductCreate.as_view(), name="create"),
    path("detail/<int:pk>", views.ProductDetail.as_view(), name="detail"),
    path("update/<int:pk>", views.ProductUpdate.as_view(), name="index"),
]
