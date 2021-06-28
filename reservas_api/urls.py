from django.urls import path
from .views import *

urlpatterns = [
    path('reservas/', ReservaListView.as_view(), name='reservas_list'),
    path('reservas/<int:pk>/', ReservaDetailView.as_view(), name='reserva_detail')
]
