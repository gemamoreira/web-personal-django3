# Generated by Django 3.0.7 on 2020-07-17 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-create'], 'verbose_name': 'proyecto', 'verbose_name_plural': 'proyectos'},
        ),
        migrations.AddField(
            model_name='project',
            name='field_name',
            field=models.URLField(blank=True, null=True, verbose_name='Dirección Web'),
        ),
        migrations.AlterField(
            model_name='project',
            name='create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='project',
            name='update',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
    ]