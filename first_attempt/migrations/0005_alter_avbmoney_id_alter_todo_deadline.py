# Generated by Django 5.1.2 on 2024-10-28 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_attempt', '0004_todo_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avbmoney',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 29, 7, 44, 9, 381450, tzinfo=datetime.timezone.utc)),
        ),
    ]
