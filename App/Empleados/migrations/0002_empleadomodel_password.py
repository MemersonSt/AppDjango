# Generated by Django 5.0.6 on 2024-05-29 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleadomodel',
            name='password',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
