from django.utils.translation import gettext as _
from django.db import models


class Label(models.Model):
    name = models.CharField(
        max_length=255, verbose_name=_('Name'),
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
