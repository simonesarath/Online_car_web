# Generated by Django 5.0.7 on 2024-09-21 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('futurcars', '0005_rename_is_available_car_available_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='available',
            new_name='is_available',
        ),
    ]
