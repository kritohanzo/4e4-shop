# Generated by Django 2.2.19 on 2023-06-08 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20230608_1718'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReadyProductSize',
            new_name='Size',
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'ordering': ['id'], 'verbose_name': 'Размер', 'verbose_name_plural': 'Размеры'},
        ),
    ]
