# Generated by Django 3.1 on 2020-08-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='balance',
            field=models.FloatField(),
        ),
    ]
