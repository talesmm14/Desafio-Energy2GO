from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from apps.hardware.models import Batery, Station


class StatusTransaction(models.IntegerChoices):
    PENDING = 1, _('PENDING')
    COMPLETED = 2, _('COMPLETED')
    ERROR = 3, _('ERROR')


class Transaction(models.Model):
    station = models.ForeignKey(Station, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=StatusTransaction.choices, default=StatusTransaction.PENDING)

    def get_absolute_url(self):
        return reverse('transaction', args=[str(self.id)])

    def __str__(self):
        return f'{self.created} - {self.get_status_display()}'
