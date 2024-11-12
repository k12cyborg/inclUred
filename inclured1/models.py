from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UsuarioManager(BaseUserManager):
    def create_user(self, correo, nombre, password=None):
        if not correo:
            raise ValueError("El usuario debe tener un correo electrónico")

        user = self.model(
            correo=self.normalize_email(correo),
            nombre=nombre,
        )
        user.set_password(password)  # Encripta la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, nombre, password=None):
        user = self.create_user(
            correo,
            nombre=nombre,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    correo = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255)
    cod_disc = models.ForeignKey(
        'Discapacidad', on_delete=models.SET_NULL, null=True, related_name='usuarios')

    # Campos adicionales
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.correo

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    @property
    def is_staff(self):
        return self.is_admin


class Discapacidad(models.Model):
    cod_disc = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Anecdota(models.Model):
    id_anecdota = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='anecdotas')
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo
