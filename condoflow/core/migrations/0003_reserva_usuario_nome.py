# Generated by Django 5.0.6 on 2024-11-04 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_remove_reserva_horario_remove_reserva_usuario_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="reserva",
            name="usuario_nome",
            field=models.CharField(default="Usuário Desconhecido", max_length=100),
        ),
    ]