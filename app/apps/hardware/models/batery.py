import uuid
from django.db import models

from apps.hardware.models.station import Station


class Batery(models.Model):
    station = models.ForeignKey(Station, on_delete=models.PROTECT)
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.code
