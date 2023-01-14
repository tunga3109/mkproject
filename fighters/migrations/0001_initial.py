# Generated by Django 4.1.4 on 2023-01-14 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=128, verbose_name='Имя героя')),
                ('descr', models.TextField(verbose_name='описание')),
                ('is_published', models.BooleanField(default=True, verbose_name='публикация')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post', verbose_name='картинка')),
            ],
            options={
                'verbose_name': 'Имя',
                'verbose_name_plural': 'Имена',
                'db_table': 'fighter_names',
                'ordering': ['-character_name'],
            },
        ),
    ]
