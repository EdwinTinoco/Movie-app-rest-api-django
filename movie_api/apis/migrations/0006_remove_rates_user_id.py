# Generated by Django 3.1 on 2020-08-08 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rates',
            name='user_id',
        ),
    ]
