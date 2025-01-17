# Generated by Django 5.0.6 on 2024-11-04 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reserva",
            name="horario",
        ),
        migrations.RemoveField(
            model_name="reserva",
            name="usuario",
        ),
        migrations.AddField(
            model_name="reserva",
            name="bloco",
            field=models.CharField(
                blank=True,
                choices=[
                    ("A", "Bloco A"),
                    ("B", "Bloco B"),
                    ("C", "Bloco C"),
                    ("D", "Bloco D"),
                    ("E", "Bloco E"),
                ],
                max_length=1,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="reserva",
            name="hora",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reserva",
            name="area",
            field=models.CharField(
                choices=[
                    ("churrasqueira", "Churrasqueira"),
                    ("piscina", "Piscina"),
                    ("quadra", "Quadra de Esporte"),
                    ("sala-de-jogos", "Sala de Jogos"),
                    ("salao-de-festa", "Salão de Festas"),
                ],
                max_length=20,
            ),
        ),
    ]
