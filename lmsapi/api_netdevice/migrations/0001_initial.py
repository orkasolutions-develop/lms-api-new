# Generated by Django 3.0.8 on 2020-07-19 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Netdevices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('producer', models.CharField(max_length=64)),
                ('model', models.CharField(max_length=32)),
                ('serialnumber', models.CharField(max_length=32)),
                ('ports', models.IntegerField()),
                ('purchasetime', models.IntegerField()),
                ('guaranteeperiod', models.PositiveIntegerField(blank=True, null=True)),
                ('shortname', models.CharField(max_length=32)),
                ('nastype', models.IntegerField()),
                ('clients', models.IntegerField()),
                ('secret', models.CharField(max_length=60)),
                ('community', models.CharField(max_length=50)),
                ('channelid', models.IntegerField(blank=True, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('hw_type', models.IntegerField()),
                ('nms_group', models.IntegerField()),
                ('wlan_freq', models.IntegerField()),
                ('wlan_ch_width', models.IntegerField()),
                ('wlan_antenna', models.IntegerField()),
                ('wlan_polarization', models.IntegerField()),
                ('wlan_cipher', models.CharField(blank=True, max_length=100, null=True)),
                ('netssid', models.CharField(max_length=32)),
                ('con_type', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'netdevices',
                'managed': False,
            },
        ),
    ]