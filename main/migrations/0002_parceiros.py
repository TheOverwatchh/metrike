# Generated by Django 3.1.7 on 2021-05-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parceiros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=25)),
                ('img_url', models.CharField(max_length=200)),
            ],
        ),
    ]
