from django.test import TestCase
from .models import Usuario, Discapacidad, Anecdota
from django.contrib.auth.hashers import check_password
from django.urls import reverse

class UsuarioModelTest(TestCase):
    def test_creacion_usuario(self):
        usuario = Usuario.objects.create(
            correo="test@example.com", 
            nombre="Test User"
        )
        self.assertEqual(usuario.correo, "test@example.com")
        self.assertEqual(usuario.nombre, "Test User")

    def test_creacion_usuario_con_password(self):
        usuario = Usuario.objects.create(
            correo="test@example.com", 
            nombre="Test User"
        )
        usuario.set_password("testpassword123")
        usuario.save()
        self.assertTrue(check_password("testpassword123", usuario.password))


class DiscapacidadModelTest(TestCase):
    def test_creacion_discapacidad(self):
        discapacidad = Discapacidad.objects.create(
            nombre="Discapacidad Auditiva", 
            descripcion="Descripción de prueba"
        )
        self.assertEqual(discapacidad.nombre, "Discapacidad Auditiva")


class UsuarioViewTest(TestCase):
    def test_usuario_list_view(self):
        response = self.client.get(reverse('usuario_list'))
        self.assertEqual(response.status_code, 200)


class UsuarioDetailViewTest(TestCase):
    def test_usuario_detail_view(self):
        usuario = Usuario.objects.create(
            correo="test@example.com",
            nombre="Test User"
        )
        response = self.client.get(reverse('usuario_detail', args=[usuario.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, usuario.nombre)


class AnecdotaModelTest(TestCase):
    def test_creacion_anecdota(self):
        usuario = Usuario.objects.create(correo="test@example.com", nombre="Test User")
        anecdota = Anecdota.objects.create(
            id_usuario=usuario,
            titulo="Anécdota de prueba",
            contenido="Contenido de la anécdota"
        )
        self.assertEqual(anecdota.titulo, "Anécdota de prueba")
        self.assertEqual(anecdota.id_usuario, usuario)
