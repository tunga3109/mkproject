# Generated by Django 4.1.4 on 2023-01-23 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelTable(
            name='profile',
            table='profiles',
        ),
    ]
