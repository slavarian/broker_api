# Generated by Django 4.2.4 on 2023-10-23 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0002_myuser_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_active',
        ),
    ]
