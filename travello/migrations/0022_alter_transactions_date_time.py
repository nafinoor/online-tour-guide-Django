# Generated by Django 4.2 on 2023-05-02 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0021_alter_transactions_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='Date_Time',
            field=models.CharField(default=datetime.datetime(2023, 5, 2, 20, 46, 43, 843478, tzinfo=datetime.timezone.utc), max_length=19),
        ),
    ]