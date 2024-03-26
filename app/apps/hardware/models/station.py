from django.db import models


class Station(models.Model):
    description = models.CharField(max_length=255)

    def is_battery_available(self):
        # TODO: Verificar no equipamento se existe uma bateria livre
        return True

    def return_battery_available(self):
        if not self.is_battery_available():
            return None
        # TODO: Retornar bateria
        return dict

    def __str__(self):
        return self.description
    