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
    path("suppliers", views.SupplierList.as_view(), name="supplier-list"),
    path("supplier/create", views.SupplierCreate.as_view(), name="supplier-create"),
    path(
        "supplier/detail/<int:pk>",
        views.SupplierDetail.as_view(),
        name="supplier-detail",
    ),
    path(
        "supplier/update/<int:pk>",
        views.SupplierUpdate.as_view(),
        name="supplier-update",
    ),
    # ==============================================
    path("orders", views.ReceiveGoodListView.as_view(), name="order-list"),
    path("order/create", views.ReceiveGoodCreateView.as_view(), name="order-create"),
    path(
        "order/detail/<int:pk>",
        views.ReceiveGoodDetailView.as_view(),
        name="order-detail",
    ),
    path(
        "order/update/<int:pk>",
        views.ReceiveGoodUpdateView.as_view(),
        name="order-update",
    ),
    # ==============================================
    path("deliveries", views.DeliveryGoodListView.as_view(), name="delivery-list"),
    path(
        "delivery/create",
        views.DeliveryGoodCreateView.as_view(),
        name="delivery-create",
    ),
    path(
        "delivery/detail/<int:pk>",
        views.DeliveryGoodDetailView.as_view(),
        name="delivery-detail",
    ),
    path(
        "delivery/update/<int:pk>",
        views.DeliveryGoodUpdateView.as_view(),
        name="delivery-update",
    ),
]
