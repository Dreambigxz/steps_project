# Generated by Django 3.0.8 on 2020-10-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userwallet', '0003_auto_20200928_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwallet',
            name='account_number',
            field=models.IntegerField(default='7716147730'),
        ),
    ]
