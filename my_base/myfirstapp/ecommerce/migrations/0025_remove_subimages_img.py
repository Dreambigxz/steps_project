# Generated by Django 3.0.8 on 2020-10-07 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0024_auto_20201007_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subimages',
            name='img',
        ),
    ]
