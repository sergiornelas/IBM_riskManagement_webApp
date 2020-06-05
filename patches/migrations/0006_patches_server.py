# Generated by Django 3.0.6 on 2020-06-03 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0004_auto_20200602_1946'),
        ('patches', '0005_remove_patches_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='patches',
            name='server',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='servers.SERVER'),
        ),
    ]