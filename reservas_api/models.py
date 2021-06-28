from django.db import models


class Reserva(models.Model):
    STATUS_CHOICES = (
        ('Pendiente', 'Pendiente'),
        ('Pagado', 'Pagado'),
        ('Eliminado', 'Eliminado')
    )
    id = models.AutoField(primary_key=True)
    habitacion = models.IntegerField(null=False)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, null=False, blank=False)
    desde = models.CharField(max_length=10)
    hasta = models.CharField(max_length=10)
    facturacion = models.CharField(max_length=250)
    id_cliente = models.CharField(max_length=8)
    monto = models.IntegerField(null=False, blank=False)
    metodo_pago = models.CharField(max_length=250)
