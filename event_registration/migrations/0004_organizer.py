# Generated by Django 5.0.1 on 2025-02-05 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration', '0003_alter_event_description_alter_event_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_registration.event')),
            ],
        ),
    ]
