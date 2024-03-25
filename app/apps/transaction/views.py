from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.transaction.models import Transaction


@api_view(['GET', 'POST'])
def receive_payment(request):
    # TODO: Verificar baterias livres
    Transaction.objects.create()
    # TODO: Enviar solicitação para equipamento via MQTT
    return Response({"message": "Transação realizada com sucesso!"})
