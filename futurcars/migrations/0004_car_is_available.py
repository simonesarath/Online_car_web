# Generated by Django 5.0.7 on 2024-09-19 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futurcars', '0003_remove_booking_test_drive_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
