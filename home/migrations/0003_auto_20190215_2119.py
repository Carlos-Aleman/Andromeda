# Generated by Django 2.1.7 on 2019-02-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190215_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etiquetas',
            name='Fecha_recibido',
            field=models.CharField(max_length=256),
        ),
    ]