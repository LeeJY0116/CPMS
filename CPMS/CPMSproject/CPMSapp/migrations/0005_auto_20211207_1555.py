# Generated by Django 3.2.9 on 2021-12-07 06:55

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CPMSapp', '0004_auto_20211205_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myticket',
            name='myPaymentDetails',
        ),
        migrations.RemoveField(
            model_name='myticket',
            name='myTicket',
        ),
        migrations.AddField(
            model_name='myticket',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 7, 6, 53, 56, 616135, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myticket',
            name='ticket_code',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myticket',
            name='ticket_name',
            field=models.CharField(default=datetime.datetime(2021, 12, 7, 6, 55, 5, 72041, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
    ]
