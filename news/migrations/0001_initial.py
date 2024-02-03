# Generated by Django 5.0 on 2024-01-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва:')),
                ('anons', models.CharField(max_length=250, verbose_name='Опис:')),
                ('haracter', models.TextField(verbose_name='Характеристики:')),
                ('date', models.DateTimeField(verbose_name='Дата публцікації')),
            ],
            options={
                'verbose_name': 'Головна сторінка ',
                'verbose_name_plural': 'Головна сторінка ',
            },
        ),
    ]