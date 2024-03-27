from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.hardware.utils import mqtt
from apps.sales.models import Transaction


@receiver(post_save, sender=Transaction)
def update_transaction_status(sender, instance, created, **kwargs):
    """ Pergunta ao equipamento via MQTT se a transação pode ser atualizada com valida. """
    if created:
        mqtt.send_message('EQUIPMENT/VALIDATION', f'transaction {{{instance.pk}}}')
