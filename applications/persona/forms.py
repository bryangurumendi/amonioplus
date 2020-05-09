from django import forms
from .models import Persona


class FormPedidoAmonio(forms.ModelForm):

    class Meta:
        model = Persona
        fields = (
            'nombre',
            'apellido',
            'correo',
            'telefono',
            'ciudad',
            'sector',
        )
