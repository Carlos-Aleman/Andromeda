# Generated by Django 2.1.7 on 2019-02-15 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190215_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='etiquetas',
            name='Precio_Reparacion',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]