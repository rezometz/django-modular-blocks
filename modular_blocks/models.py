from django.db import models

from .fields import ListTextField


class TwoModularColumnsMixin(models.Model):
    sidebar_left = ListTextField(
        blank=True,
        null=True,
    )
    sidebar_right = ListTextField(
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True
