# Generated by Django 3.0.7 on 2020-07-17 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_project_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='link',
        ),
    ]
