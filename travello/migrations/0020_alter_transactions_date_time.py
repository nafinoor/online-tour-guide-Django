# Generated by Django 4.2 on 2023-05-02 19:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0019_alter_transactions_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='Date_Time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
