# Generated by Django 3.0.8 on 2020-10-20 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tradeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paid_user',
            old_name='amount_received',
            new_name='amount_receive',
        ),
    ]
