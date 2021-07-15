from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("stores.urls", namespace="stores")),
    path("admin/", admin.site.urls),
]
