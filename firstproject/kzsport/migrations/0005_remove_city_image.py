# Generated by Django 4.0.2 on 2022-03-16 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kzsport', '0004_city_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='image',
        ),
    ]
