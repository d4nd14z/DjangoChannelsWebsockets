from django.db import models
from .categoria import Categoria

class Producto (models.Model):

    id = models.BigAutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    imagen = models.CharField(max_length=512)
    precio = models.FloatField()
    disponible = models.IntegerField()
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL)
    status = models.BooleanField(default=True)

    class Meta: 
        app_label = 'api'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return str(self.id)