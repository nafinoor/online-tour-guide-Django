# Generated by Django 4.2 on 2023-06-05 08:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0025_alter_pessanger_detail_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='Date_Time',
            field=models.CharField(default=datetime.datetime(2023, 6, 5, 8, 16, 59, 311131, tzinfo=datetime.timezone.utc), max_length=19),
        ),
    ]
