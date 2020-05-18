# Generated by Django 3.0.6 on 2020-05-05 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_package', models.CharField(max_length=30)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('criticality', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
