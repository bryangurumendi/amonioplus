from django.shortcuts import render
from django.views.generic import CreateView
from .models import Persona
from .forms import FormPedidoAmonio
from applications.producto.models import Producto

# Create your views here.


class PedidoAmonio(CreateView):
    model = Persona
    template_name = "index2.html"
    form_class = FormPedidoAmonio
    success_url = "#"

    def form_valid(self, form):
        cliente = form.save()
        print(cliente)
        cliente.save()
        return super(PedidoAmonio, self).form_valid(form)

