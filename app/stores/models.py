from django.db import models
from mixins.assets import TimeStampMixin


class Category(TimeStampMixin):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="categories/images", blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        db_table = "categories"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Supplier(TimeStampMixin):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True, blank=True)
    phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(TimeStampMixin):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    qty_received = models.IntegerField(default=0)
    qty_ordered = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    date_received = models.DateField(null=True)
    purchase_order = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
