from django.db import models

from .fields import ListTextField


class TwoModularColumnsMixin(models.Model):
    sidebar_left = ListTextField()
    sidebar_right = ListTextField()

    class Meta:
        abstract = True
