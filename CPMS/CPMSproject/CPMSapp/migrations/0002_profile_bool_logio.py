# Generated by Django 3.2.9 on 2021-12-05 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPMSapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bool_logIO',
            field=models.BooleanField(default=False),
        ),
    ]