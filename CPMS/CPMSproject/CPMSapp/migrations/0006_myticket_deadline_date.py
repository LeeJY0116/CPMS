# Generated by Django 3.2.9 on 2021-12-07 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPMSapp', '0005_auto_20211207_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='myticket',
            name='deadline_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]