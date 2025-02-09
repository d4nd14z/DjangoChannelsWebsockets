from django.contrib import admin
from .models.producto import Producto
from .models.categoria import Categoria
from .models.orden_master import OrdenMaster
from .models.orden_detail import OrdenDetail

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin): 
    list_display = ['id', 'nombre', 'precio', 'disponible', 'status']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'status']

@admin.register(OrdenMaster)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha', 'valor_total', 'status']

@admin.register(OrdenDetail)
class OrdenDetail(admin.ModelAdmin):
    list_display = ['id', 'fecha', 'producto', 'cantidad', 'valor', 'status']

