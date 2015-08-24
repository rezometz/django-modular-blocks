from django.db import models

from .fields import ListTextField


class TwoModularColumnsMixin(models.Model):
    sidebar_left = ListTextField(
        blank=True,
        null=True,
    )
    sidebar_right = ListTextField(
        lank=True,
        null=True,
    )

    class Meta:
        abstract = True
