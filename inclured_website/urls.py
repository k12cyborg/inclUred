from django.contrib import admin
from django.urls import path, include
from inclured1 import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Página de inicio en la URL principal
    path('', views.index, name="index"),

    # Incluye las URLs de `inclured1`
    path('inclured1/', include("inclured1.urls")),

    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    path('perfil/', views.perfil, name='perfil'),

    # URLs para las secciones principales de la página
    path('informacion/', views.informacion, name='informacion'),
    path('anecdotas/', views.anecdotas, name='anecdotas'),
    path('cursos/', views.cursos, name='cursos'),
    path('videos/', views.videos_informativos, name='videos'),

    # URLs para Usuario
    path('usuarios/', views.UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario_detail'),

    # URLs para Discapacidad
    path('discapacidades/', views.DiscapacidadListView.as_view(), name='discapacidad_list'),
    path('discapacidades/<int:pk>/', views.DiscapacidadDetailView.as_view(), name='discapacidad_detail'),

    # URLs para Anecdota
    path('anecdotas-list/', views.AnecdotaListView.as_view(), name='anecdota_list'),
    path('anecdotas-list/<int:pk>/', views.AnecdotaDetailView.as_view(), name='anecdota_detail'),
    path('anecdotas/crear/', views.crear_anecdota, name='crear_anecdota'),  # Nueva URL para crear anécdota
]
