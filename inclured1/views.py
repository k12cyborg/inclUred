from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Usuario, Discapacidad, Anecdota

# Vista para la página de inicio
def index(request):
    return render(request, "index.html")

# Vista para la sección de Información
def informacion(request):
    return render(request, "informacion.html")

# Vista para la sección de Cursos
def cursos(request):
    return render(request, "cursos.html")

# Vista para la sección de Videos Informativos
def videos_informativos(request):
    return render(request, "videos_informativos.html")

# Vista para la sección de Anécdotas
def anecdotas(request):
    return render(request, "anecdotas.html")

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
