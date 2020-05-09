from django.db import models

# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.nombre


class Unidade(models.Model):

    unidad = models.CharField(
        max_length=50,
        default="Unidad",
    )

    def __str__(self):
        return self.unidad


class Producto(models.Model):

    imagen = models.ImageField(upload_to='producto', blank=True)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    unidad = models.ForeignKey(
        Unidade,
        on_delete=models.CASCADE
    )

    codigo = models.CharField(
        max_length=50,
    )

    nombre = models.CharField(
        max_length=50,
    )

    descripcion = models.CharField(
        max_length=500,
        blank=True,
    )

    precio = models.IntegerField()

    veces_pedido = models.PositiveIntegerField(default=0)

    SIMPLE = 's'
    COMPUESTO = 'c'
    TIPO_ = (
        (SIMPLE, 'Simple'),
        (COMPUESTO, 'Compuesto'),
    )

    tipo = models.CharField(
        max_length=50,
        choices=TIPO_
    )

    def __str__(self):
        return self.nombre + ' - ' + self.codigo
