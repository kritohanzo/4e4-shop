# Generated by Django 2.2.19 on 2023-06-13 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workzone', '0002_auto_20230613_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='worker',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='works_in_process', to=settings.AUTH_USER_MODEL),
        ),
    ]
