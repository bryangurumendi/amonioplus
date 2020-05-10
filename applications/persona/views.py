from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import (
    FormView,
)
from .models import Persona
from .forms import FormPedidoAmonio
from applications.producto.models import Producto

# Create your views here.


class PedidoAmonio(FormView):
    model = Persona
    template_name = "index2.html"
    form_class = FormPedidoAmonio
    success_url = 'succesfull'

    def form_valid(self, form):
        cliente = form.save()
        print(cliente)
        cliente.save()
        return super(PedidoAmonio, self).form_valid(form)

    

class Exitoso(TemplateView):
    template_name = "registro.html"

