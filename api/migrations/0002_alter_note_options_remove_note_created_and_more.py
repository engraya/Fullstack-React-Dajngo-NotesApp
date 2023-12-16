# Generated by Django 5.0 on 2023-12-16 14:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['createdAt', 'updatedAt']},
        ),
        migrations.RemoveField(
            model_name='note',
            name='created',
        ),
        migrations.AddField(
            model_name='note',
            name='createdAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='note',
            name='updatedAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
