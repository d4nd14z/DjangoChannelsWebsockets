from django.db import models

class OrdenMaster (models.Model): 

    id = models.BigAutoField(primary_key=True, null=False)
    fecha = models.DateTimeField(auto_now_add=True)
    valor_total = models.FloatField()    
    status = models.BooleanField(default=True)

    class Meta: 
        app_label = 'api'
        verbose_name = 'Orden de Compra'
        verbose_name_plural = 'Ordenes de Compra'

    def __str__(self):
        return str(self.id)
