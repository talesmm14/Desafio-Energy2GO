import re

from apps.hardware.utils.mqtt import subscribe_topic
from apps.sales.models import Transaction, StatusTransaction
from config.celery import app


@app.task(name='sales.tasks.transaction_confirmations')
def transaction_confirmations() -> None:
    def on_message(client, userdata, message) -> None:
        msg = message.payload.decode()
        if match := re.search(r'{(\d+)}', msg):
            transaction_id = match.group(1)
            if transaction := Transaction.objects.filter(id=transaction_id).first():
                if msg.startswith("confirm transaction"):
                    transaction.status = StatusTransaction.COMPLETED
                else:
                    transaction.status = StatusTransaction.ERROR
                transaction.save()
    subscribe_topic('EQUIPMENT/VALIDATION/RESPONSE', on_message)
