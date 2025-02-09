from django.db import models
from .producto import Producto
from .orden_master import OrdenMaster

class OrdenDetail (models.Model): 

    id = models.BigAutoField(primary_key=True, null=False)
    fecha = models.DateTimeField(auto_now_add=True)
    master = models.ForeignKey(OrdenMaster, null=True, on_delete=models.SET_NULL)
    producto = models.ForeignKey(Producto, null=True, on_delete=models.SET_NULL)
    cantidad = models.IntegerField()
    valor = models.FloatField()
    status = models.BooleanField(default=True)
    
    class Meta: 
        app_label = 'api'
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalles de Compra'

    def __str__(self):
        return str(self.id)
