# Generated by Django 5.1.1 on 2024-09-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='comment',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
    ]
