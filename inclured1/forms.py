from django import forms
from .models import Usuario, Discapacidad, Anecdota
from django.contrib.auth.forms import AuthenticationForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['correo', 'nombre', 'cod_disc', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'cod_disc': 'Discapacidad',  # Etiqueta personalizada
        }
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['cod_disc'].queryset = Discapacidad.objects.all()  # Para que muestre todas las discapacidades en el formulario

class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class AnecdotaForm(forms.ModelForm):
    class Meta:
        model = Anecdota
        fields = ['titulo', 'contenido']  # Excluye id_usuario porque será asignado automáticamente

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu anécdota aquí...'}),
        }
