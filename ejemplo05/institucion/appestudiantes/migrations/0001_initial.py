# Generated by Django 4.0.5 on 2022-06-13 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('cedula', models.CharField(max_length=30, unique=True)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
