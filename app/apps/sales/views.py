from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.hardware.models import Station
from apps.sales.models import Transaction
from apps.sales.serializers import TransactionSerializer


@api_view(['GET'])
def transactions(request):
    ts = Transaction.objects.all()
    serializer = TransactionSerializer(ts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def transaction(request, pk: int):
    t = get_object_or_404(Transaction, pk=pk)
    serializer = TransactionSerializer(t)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(
    methods=['POST'], operation_summary="Receive Payment API", tags=['sales'],
    responses={200: "Transação realizada com sucesso!", 500: "Sem baterias para realizar!"}
)
@api_view(['POST'])
def receive_payment(request, pk: int):
    station: Station = get_object_or_404(Station, pk=pk)
    if station.is_battery_available():
        transaction = Transaction.objects.create(station=station)
        return Response(
            {
                "message": "Transação realizada com sucesso!",
                "transacao": request.build_absolute_uri(transaction.get_absolute_url())
            },
            status=status.HTTP_200_OK
        )
    return Response({"message": "Sem baterias para realizar!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
