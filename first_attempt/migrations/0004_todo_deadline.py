# Generated by Django 5.1.2 on 2024-10-28 07:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_attempt', '0003_avbmoney'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 29, 7, 25, 18, 203002, tzinfo=datetime.timezone.utc)),
        ),
    ]