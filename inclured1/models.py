from django.db import models

class Usuarios(models.Model):

    # Campos
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.TextField(help_text="Ingresa un nombre de ususario", null=False)
    correo = models.EmailField(help_text="Ingresa tu correo", null=False)
    contrasena = models.TextField(help_text="Ingreso una contraseña", null=False)
    discapacidad = models.TextField(help_text="Ingresa tu discapacidad", null=False)
    ...

    def __str__(self):
        return self.nombre

class Perfiles(models.Model):

    # Campos
    id_perfil = models.IntegerField(primary_key=True)
    id_usuario = models.IntegerField()
    # imagen = models.ImageField(help_text="Imagen de perfil", null=True)
    ...

    def __str__(self):
        return self.id_perfil
      
class Anecdotas(models.Model):

    # Campos
    id_anecdota = models.IntegerField(primary_key=True)
    id_usuario = models.IntegerField()
    titulo = models.TextField(help_text="Ingresa un titulo para la anecdota", null=False)
    contenido = models.TextField(help_text="Ingresa el contenido para la anecdota", null=False)
    
    # imagen = models.ImageField(help_text="Imagen de perfil", null=True)
    ...

    def __str__(self):
        return self.titulo

class Informaciones(models.Model):

    # Campos
    id_informacion = models.IntegerField(primary_key=True)
    titulo = models.TextField(help_text="Ingresa un titulo para la anecdota", null=False)
    subtitulo = models.TextField(help_text="Ingresa un subtitulo para la anecdota", null=False)
    contenido = models.TextField(help_text="Ingresa el contenido para la anecdota", null=False)
    
    # imagen = models.ImageField(help_text="Imagen de perfil", null=True)
    ...

    def __str__(self):
        return self.titulo
