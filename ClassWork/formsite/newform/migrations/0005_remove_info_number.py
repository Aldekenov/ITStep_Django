# Generated by Django 4.2 on 2023-07-19 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newform', '0004_remove_info_stud_id_info_id_alter_info_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='number',
        ),
    ]
