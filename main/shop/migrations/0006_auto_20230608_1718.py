# Generated by Django 2.2.19 on 2023-06-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20230608_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadyProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Размер продукта',
                'verbose_name_plural': 'Размеры продуктов',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='readyproduct',
            name='color',
            field=models.CharField(default='-нет-', max_length=64, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='readyproduct',
            name='description',
            field=models.CharField(default='-нет-', max_length=640, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='readyproduct',
            name='model',
            field=models.CharField(max_length=64, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='readyproduct',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Наименовение'),
        ),
        migrations.AddField(
            model_name='readyproduct',
            name='size',
            field=models.ManyToManyField(to='shop.ReadyProductSize', verbose_name='Размер'),
        ),
    ]
