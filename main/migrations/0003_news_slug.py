# Generated by Django 3.1.7 on 2021-05-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_parceiros'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='slug_padrao'),
        ),
    ]