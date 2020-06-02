# Generated by Django 3.0.6 on 2020-06-02 18:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exception', '0002_approve_exception'),
    ]

    operations = [
        migrations.CreateModel(
            name='EXCEPTION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=8)),
                ('title', models.CharField(max_length=30)),
                ('justification', models.TextField()),
                ('action_plan', models.TextField()),
                ('exclude_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='AUTHORIZE_EXCEPTION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exception_id', models.IntegerField(null=True)),
                ('state', models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=8)),
                ('comment', models.TextField(blank=True, default='Pending')),
                ('approver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
