# Generated by Django 2.2.19 on 2023-06-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20230608_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_code',
            field=models.IntegerField(default=340701, verbose_name='Код подтверждения'),
        ),
    ]