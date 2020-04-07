# Generated by Django 3.0.5 on 2020-04-06 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patches', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exceptions', '0004_exclude_patch_patchfrom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exclude_patch',
            name='patchFrom',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patches.patch'),
        ),
        migrations.AlterField(
            model_name='exclude_patch',
            name='userID',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]