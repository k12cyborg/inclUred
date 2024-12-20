from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import Usuario, Discapacidad, Anecdota
from .forms import UsuarioForm, LoginForm, AnecdotaForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Vista para el registro
def register_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect("index")  # Cambia 'pagina_principal' por tu vista principal
    else:
        form = UsuarioForm()

    return render(request, 'register.html', {'form': form})

# Vista para iniciar sesión
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            correo = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=correo, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")  # Cambia 'pagina_principal' por tu vista principal
            else:
                messages.error(request, "Correo o contraseña incorrectos")
        else:
            messages.error(request, "Formulario no válido")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# Vista para cerrar sesión
@csrf_exempt
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"message": "Sesión cerrada con éxito"}, status=200)
    return JsonResponse({"error": "Método no permitido"}, status=405)

# Vista para el perfil del usuario
def perfil(request):
    return render(request, "perfil.html")

# Vista para la página de inicio
def index(request):
    return render(request, "index.html")

# Vista para la sección de Información
def informacion(request):
    return render(request, "informacion.html")

# Vista para las sección de Anécdotas
@login_required
def anecdotas(request):
    anecdotas = Anecdota.objects.select_related('id_usuario').all()
    if request.method == 'POST':
        form = AnecdotaForm(request.POST)
        if form.is_valid():
            anecdota = form.save(commit=False)
            anecdota.id_usuario = request.user  # Asigna el usuario logueado
            anecdota.save()
    else:
        form = AnecdotaForm()
    
    return render(request, 'anecdotas.html', {'anecdotas': anecdotas, 'form': form})

# Vista para crear una anécdota
@login_required
def crear_anecdota(request):
    if request.method == 'POST':
        form = AnecdotaForm(request.POST)
        if form.is_valid():
            anecdota = form.save(commit=False)
            anecdota.id_usuario = request.user  # Asigna el usuario logueado
            anecdota.save()
            return redirect('anecdotas')  # Redirige a la página de anécdotas
    else:
        form = AnecdotaForm()
    return render(request, 'crear_anecdota.html', {'form': form})

# Vista para la sección de Cursos
def cursos(request):
    return render(request, "cursos.html")

# Vista para la sección de Videos Informativos
def videos_informativos(request):
    return render(request, "videos_informativos.html")

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
