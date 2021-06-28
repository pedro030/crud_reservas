from rest_framework import serializers


class ReservaSerializer(serializers.Serializer):

    habitacion = serializers.IntegerField()
    estado = serializers.CharField(
        max_length=20)
    desde = serializers.CharField(max_length=10)
    hasta = serializers.CharField(max_length=10)
    facturacion = serializers.CharField(max_length=250)
    id_cliente = serializers.CharField(max_length=8)
    monto = serializers.IntegerField()
    metodo_pago = serializers.CharField(max_length=250)
