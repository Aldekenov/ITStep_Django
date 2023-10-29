# Generated by Django 4.2 on 2023-07-19 15:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newform', '0005_remove_info_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='number',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(10000000000, message='номер введен не корректно'), django.core.validators.MaxValueValidator(100000000000, message='номер введен не корректно')], verbose_name='Номер телефона'),
        ),
    ]