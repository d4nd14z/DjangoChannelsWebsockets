from django.db import models

class Categoria (models.Model):

    id = models.BigAutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    status = models.BooleanField(default=True)

    class Meta:
        app_label = 'api'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre