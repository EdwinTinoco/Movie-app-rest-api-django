# Generated by Django 3.1 on 2020-08-10 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0008_userauth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='movies',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
