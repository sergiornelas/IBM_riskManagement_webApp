# Generated by Django 3.0.2 on 2020-02-24 03:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exclude_patch',
            name='excludeDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='exclude_patch',
            name='justification',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='patch',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]