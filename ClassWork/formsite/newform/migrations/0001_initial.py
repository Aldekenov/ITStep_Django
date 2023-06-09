# Generated by Django 4.2 on 2023-06-23 15:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3, message='Минимум 3 символов')], verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3, message='Минимум 3 символов')], verbose_name='Фамилия')),
                ('birthday', models.DateField(db_index=True, verbose_name='Дата рождения')),
                ('number', models.FloatField(blank=True, null=True, verbose_name='Номер телефона')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='newform.lesson', verbose_name='Курс')),
            ],
        ),
    ]
