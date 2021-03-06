# Generated by Django 3.0.7 on 2020-08-14 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoutersType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'routerstype',
            },
        ),
        migrations.CreateModel(
            name='Routers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=255)),
                ('port', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('identity', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modify', models.DateTimeField(auto_now=True, null=True)),
                ('lastbackup', models.DateTimeField(blank=True, null=True)),
                ('sleeptime', models.SmallIntegerField()),
                ('isActivated', models.BooleanField(default=False)),
                ('devtype', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='api_rbbackup.RoutersType')),
            ],
            options={
                'db_table': 'routers',
            },
        ),
    ]
