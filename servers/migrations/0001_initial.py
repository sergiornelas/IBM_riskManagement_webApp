# Generated by Django 3.0.6 on 2020-06-02 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SERVER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=30)),
                ('os', models.CharField(max_length=30)),
                ('reboot_required', models.CharField(default='False', max_length=5)),
                ('domain', models.CharField(default='ibmcloud.dst.ibm.com', max_length=30)),
                ('ansible_id', models.PositiveSmallIntegerField(default=1)),
                ('carbon_black', models.CharField(default='N/A', max_length=5)),
                ('crowd_strike', models.CharField(default='N/A', max_length=5)),
                ('big_fix', models.CharField(default='True', max_length=5)),
            ],
        ),
    ]