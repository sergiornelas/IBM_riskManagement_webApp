# Generated by Django 3.0.6 on 2020-08-03 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patches', '0003_auto_20200803_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='patches',
            name='exception_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patches',
            name='patched_date',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
