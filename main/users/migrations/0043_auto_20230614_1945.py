# Generated by Django 2.2.19 on 2023-06-14 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_auto_20230614_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_code',
            field=models.IntegerField(default=379414, verbose_name='Код подтверждения'),
        ),
    ]
