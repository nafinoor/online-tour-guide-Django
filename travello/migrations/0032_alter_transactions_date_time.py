# Generated by Django 4.2 on 2023-06-17 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0031_alter_transactions_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='Date_Time',
            field=models.CharField(default=datetime.datetime(2023, 6, 17, 18, 24, 14, 76674, tzinfo=datetime.timezone.utc), max_length=256),
        ),
    ]
