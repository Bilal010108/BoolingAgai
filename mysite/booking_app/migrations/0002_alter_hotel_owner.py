# Generated by Django 5.1.4 on 2024-12-15 09:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]