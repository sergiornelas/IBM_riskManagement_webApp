# Generated by Django 3.0.6 on 2020-07-04 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exception', '0015_auto_20200704_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validate_exception',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]