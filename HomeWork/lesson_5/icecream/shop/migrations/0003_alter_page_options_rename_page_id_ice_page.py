# Generated by Django 4.1.4 on 2023-06-09 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_page_ice_page_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['number'], 'verbose_name': 'Страница', 'verbose_name_plural': 'Страница'},
        ),
        migrations.RenameField(
            model_name='ice',
            old_name='page_id',
            new_name='page',
        ),
    ]
