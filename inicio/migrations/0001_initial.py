# Generated by Django 4.1.7 on 2023-04-14 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('stock', models.IntegerField()),
                ('fecha_de_carga', models.DateField()),
            ],
        ),
    ]
