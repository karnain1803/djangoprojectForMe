# Generated by Django 4.1.4 on 2023-01-01 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='data_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]