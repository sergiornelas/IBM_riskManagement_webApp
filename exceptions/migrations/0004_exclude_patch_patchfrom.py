# Generated by Django 3.0.5 on 2020-04-06 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patches', '0001_initial'),
        ('exceptions', '0003_auto_20200406_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='exclude_patch',
            name='patchFrom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patches.patch'),
        ),
    ]