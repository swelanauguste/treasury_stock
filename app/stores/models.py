from django.db import models
from django.urls import reverse
from mixins.assets import TimeStampMixin
from django.utils.text import slugify


class Category(TimeStampMixin):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="categories/images", blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        db_table = "categories"
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Supplier(TimeStampMixin):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True, blank=True)
    phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Supplier, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("stores:supplier-detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("stores:supplier-update", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Product(TimeStampMixin):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.SET_NULL, null=True
    )
    supplier = models.ForeignKey(
        Supplier, related_name="product_suppliers", on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    qty = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("stores:product-detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("stores:product-update", kwargs={"pk": self.pk})

    def get_total_quantity(self):
        return (
            sum(item.get_received_quantity() for item in self.received_goods.all())
            + self.qty
        ) - (sum(item.get_delivered_quantity() for item in self.delivered_goods.all()))

    def __str__(self):
        return self.name


def purchase_order_path(instance, filename):
    return "purchase_orders/%s/%s" % (instance.pk, filename)


class ReceiveGood(TimeStampMixin):
    product = models.ForeignKey(
        Product, related_name="received_goods", on_delete=models.SET_NULL, null=True
    )
    qty = models.IntegerField(default=0)
    received_date = models.DateField(blank=True, null=True)
    received_by = models.CharField(max_length=100, blank=True, null=True)
    received_from = models.CharField(max_length=100, blank=True, null=True)
    received_comment = models.TextField(blank=True, null=True)
    purchase_order_number = models.CharField(max_length=100, blank=True, null=True)
    purchase_order = models.FileField(
        blank=True, null=True, upload_to=purchase_order_path
    )

    def get_absolute_url(self):
        return reverse("stores:order-detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("stores:order-update", kwargs={"pk": self.pk})

    def get_received_quantity(self):
        return self.qty

    def get_balance(self):
        return self.product.qty

    def __str__(self):
        return "%s %s" % (self.product.name, self.qty)


class DeliveryGood(TimeStampMixin):
    product = models.ForeignKey(
        Product, related_name="delivered_goods", on_delete=models.SET_NULL, null=True
    )
    qty = models.IntegerField(default=0)
    delivery_date = models.DateField(blank=True, null=True)
    delivery_to = models.CharField(max_length=100, blank=True, null=True)
    delivery_from = models.CharField(max_length=100, blank=True, null=True)
    delivery_comment = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("stores:delivery-detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("stores:delivery-update", kwargs={"pk": self.pk})

    def get_delivered_quantity(self):
        return self.qty

    def get_balance(self):
        return self.product.qty

    def __str__(self):
        return "%s %s" % (self.product.name, self.qty)
