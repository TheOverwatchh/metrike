# Generated by Django 3.1.7 on 2021-05-08 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]