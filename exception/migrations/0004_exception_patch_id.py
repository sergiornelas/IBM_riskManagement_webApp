# Generated by Django 3.0.6 on 2020-06-02 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exception', '0003_authorize_exception_exception'),
    ]

    operations = [
        migrations.AddField(
            model_name='exception',
            name='patch_id',
            field=models.IntegerField(null=True),
        ),
    ]
