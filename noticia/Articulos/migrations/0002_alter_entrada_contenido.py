# Generated by Django 4.0.6 on 2022-07-06 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='contenido',
            field=models.TextField(max_length=500),
        ),
    ]
