# Generated by Django 2.2.19 on 2023-06-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20230609_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_code',
            field=models.IntegerField(default=664322, verbose_name='Код подтверждения'),
        ),
    ]
