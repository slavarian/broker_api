# Generated by Django 4.2.4 on 2023-10-23 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyshares', '0003_alter_shares_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='shares',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='кол-во акций'),
            preserve_default=False,
        ),
    ]
