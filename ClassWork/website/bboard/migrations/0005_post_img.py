# Generated by Django 4.2.6 on 2023-10-30 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0004_delete_currentpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='product', verbose_name='Изображение'),
        ),
    ]
