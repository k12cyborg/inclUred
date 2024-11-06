from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Usuario, Discapacidad, Anecdota

# Create your views here.
# Listar usuarios


class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/usuario_list.html'
    context_object_name = 'usuarios'

# Ver detalles de un usuario


class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuarios/usuario_detail.html'
    context_object_name = 'usuario'


# Listar discapacidades
class DiscapacidadListView(ListView):
    model = Discapacidad
    template_name = 'discapacidades/discapacidad_list.html'
    context_object_name = 'discapacidades'

# Ver detalles de una discapacidad


class DiscapacidadDetailView(DetailView):
    model = Discapacidad
    template_name = 'discapacidades/discapacidad_detail.html'
    context_object_name = 'discapacidad'

# Listar anécdotas


class AnecdotaListView(ListView):
    model = Anecdota
    template_name = 'anecdotas/anecdota_list.html'
    context_object_name = 'anecdotas'

# Ver detalles de una anécdota


class AnecdotaDetailView(DetailView):
    model = Anecdota
    template_name = 'anecdotas/anecdota_detail.html'
    context_object_name = 'anecdota'


def index(request):
    return render(request, "index.html")
