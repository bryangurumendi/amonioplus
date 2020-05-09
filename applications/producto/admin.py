from django.contrib import admin
from .models import Categoria, Producto, Unidade

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'categoria',
        'precio',
        'unidad',
    )


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
admin.site.register(Unidade)