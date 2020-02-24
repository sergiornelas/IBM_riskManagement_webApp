# Generated by Django 3.0.2 on 2020-02-24 03:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='exclude_patch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('justification', models.TextField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='patch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_package', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('criticality', models.CharField(max_length=30)),
            ],
        ),
    ]
