from django import forms
from .models import Usuario, Discapacidad

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['correo', 'nombre', 'cod_disc', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['cod_disc'].queryset = Discapacidad.objects.all()  # Para que muestre todas las discapacidades en el formulario
