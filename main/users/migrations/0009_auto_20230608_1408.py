# Generated by Django 2.2.19 on 2023-06-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20230608_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_code',
            field=models.IntegerField(default=404269, verbose_name='Код подтверждения'),
        ),
    ]
