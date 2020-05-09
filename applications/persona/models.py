from django.db import models

# Create your models here.

class Persona(models.Model):

    nombre = models.CharField(
        'nombre',
        max_length=50,
    )

    apellido = models.CharField(
        'apellido',
        max_length=50,
    )

    correo = models.EmailField(
        'correo',
        max_length=254,
    )

    GUAYAQUIL = 'gye'

    CIUDAD_ = (
        (GUAYAQUIL, 'Guayaquil'),
    )

    ciudad = models.CharField(
        'ciudad',
        max_length=50,
        choices=CIUDAD_,
        blank=True
    )

    SUR = 'sur'
    SURESTE = 'sur_e'
    CENTRO = 'cen'
    NORTE = 'nor'
    SAMBO = 'samb'

    SECTOR_ = (
        (SUR, 'Sur'),
        (SURESTE, 'Sur-Este'),
        (CENTRO, 'Centro'),
        (NORTE, 'Norte'),
        (SAMBO, 'Samborondon'),
    )

    sector = models.CharField(
        'sector',
        max_length=50,
        choices=SECTOR_,
    )

    direccion = models.CharField(
        'direccion',
        max_length=500,
    )

    telefono = models.CharField(
        'telefono',
        max_length=10,
    )

    def __str__(self):
        return self.nombre + ' ' + self.apellido