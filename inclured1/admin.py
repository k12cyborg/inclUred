from django.contrib import admin
from .models import Usuario, Discapacidad, Anecdota

# Registrar modelos en el panel de administración
admin.site.register(Usuario)
admin.site.register(Discapacidad)
admin.site.register(Anecdota)
