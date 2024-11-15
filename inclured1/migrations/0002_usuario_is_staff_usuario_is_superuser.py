# Generated by Django 5.1.1 on 2024-11-15 20:02

from django.db import migrations, models


def cargar_datos_disca(apps, schema_editor):
    Discapacidad = apps.get_model('inclured1', 'Discapacidad')
    # Crear los datos predeterminados
    Discapacidad.objects.get_or_create(
        nombre='Discapacidad Visual', descripcion='Pérdida total o parcial de la visión.')
    Discapacidad.objects.get_or_create(
        nombre='Discapacidad Auditiva', descripcion='Pérdida total o parcial de la audición.')
    Discapacidad.objects.get_or_create(
        nombre='Discapacidad Motriz', descripcion='Limitación en el movimiento de alguna parte del cuerpo.')
    Discapacidad.objects.get_or_create(
        nombre='Discapacidad Cognitiva', descripcion='Trastorno que afecta las capacidades mentales y de aprendizaje.')


class Migration(migrations.Migration):

    dependencies = [
        ('inclured1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(cargar_datos_disca),
    ]
