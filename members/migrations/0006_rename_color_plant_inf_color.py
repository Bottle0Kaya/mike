# Generated by Django 4.1 on 2022-09-08 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_plant_inf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant_inf',
            old_name='color',
            new_name='Color',
        ),
    ]
