# Generated by Django 3.1 on 2020-08-09 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_auto_20200809_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_auth', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user_authorization',
            },
        ),
    ]