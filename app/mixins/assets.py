from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class TimeStampMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, null=True,
        related_name="%(class)s_created", default=1
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, null=True,
        related_name="%(class)s_updated", default=1
    )

    class Meta:
        abstract = True
