# Generated by Django 3.0.7 on 2020-07-17 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200716_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='field_name',
        ),
        migrations.AddField(
            model_name='project',
            name='enlace',
            field=models.URLField(blank=True, null=True, verbose_name='Dirección Web'),
        ),
    ]
