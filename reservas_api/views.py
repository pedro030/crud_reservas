from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework import status
from reservas_api import serializers
from .models import *


class ReservaListView(APIView):
    """ API view de las reservas """
    serializer_class = serializers.ReservaSerializer

    def get(self, request):
        """ retorna el listado de reservas """
        lista = Reserva.objects.all()
        return Response({"reservas": lista.values()})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            habitacion = serializer.validated_data.get('habitacion')
            estado = serializer.validated_data.get('estado')
            desde = serializer.validated_data.get('desde')
            hasta = serializer.validated_data.get('hasta')
            facturacion = serializer.validated_data.get('facturacion')
            id_cliente = serializer.validated_data.get('id_cliente')
            monto = serializer.validated_data.get('monto')
            metodo_pago = serializer.validated_data.get('metodo_pago')
            reserva = Reserva(habitacion=habitacion, status=estado, desde=desde, hasta=hasta,
                              facturacion=facturacion, id_cliente=id_cliente, monto=monto, metodo_pago=metodo_pago)
            reserva.save()
            return Response({"message": "created", "reserva": model_to_dict(reserva)})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class ReservaDetailView(APIView):
    """ API view de las reservas """
    serializer_class = serializers.ReservaSerializer

    def get(self, request, pk):
        """ retorna el listado de reservas """
        reserva = Reserva.objects.get(pk=pk)
        return Response(model_to_dict(reserva))

    def delete(self, request, pk):
        reserva = Reserva.objects.get(pk=pk)
        reserva.delete()
        return Response({"message": "deleted"})

    def put(self, request, pk):
        reserva = Reserva.objects.filter(pk=pk).first()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            reserva.habitacion = serializer.validated_data.get('habitacion')
            reserva.estado = serializer.validated_data.get('estado')
            reserva.desde = serializer.validated_data.get('desde')
            reserva.hasta = serializer.validated_data.get('hasta')
            reserva.facturacion = serializer.validated_data.get('facturacion')
            reserva.id_cliente = serializer.validated_data.get('id_cliente')
            reserva.monto = serializer.validated_data.get('monto')
            reserva.metodo_pago = serializer.validated_data.get('metodo_pago')
            reserva.save()
        return Response(model_to_dict(reserva))
