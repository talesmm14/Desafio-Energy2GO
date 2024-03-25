from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusTransaction(models.IntegerChoices):
    PENDING = 1, _('PENDING')
    COMPLETED = 2, _('COMPLETED')
    ERROR = 3, _('ERROR')


class Transaction(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=StatusTransaction.choices, default=StatusTransaction.PENDING)

    def __str__(self):
        return f'{self.created} - {self.get_status_display()}'
