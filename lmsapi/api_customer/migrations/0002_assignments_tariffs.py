# Generated by Django 3.0.7 on 2020-09-27 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liabilityid', models.IntegerField()),
                ('period', models.SmallIntegerField()),
                ('at', models.IntegerField()),
                ('datefrom', models.IntegerField()),
                ('dateto', models.IntegerField()),
                ('invoice', models.IntegerField()),
                ('suspended', models.IntegerField()),
                ('settlement', models.IntegerField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=4)),
                ('paytype', models.SmallIntegerField(blank=True, null=True)),
                ('numberplanid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'assignments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tariffs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('type', models.IntegerField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=9)),
                ('taxid', models.IntegerField()),
                ('prodid', models.CharField(max_length=255)),
                ('uprate', models.IntegerField()),
                ('upceil', models.IntegerField()),
                ('downrate', models.IntegerField()),
                ('downceil', models.IntegerField()),
                ('climit', models.IntegerField()),
                ('plimit', models.IntegerField()),
                ('dlimit', models.IntegerField()),
                ('domain_limit', models.IntegerField(blank=True, null=True)),
                ('alias_limit', models.IntegerField(blank=True, null=True)),
                ('sh_limit', models.IntegerField(blank=True, null=True)),
                ('www_limit', models.IntegerField(blank=True, null=True)),
                ('mail_limit', models.IntegerField(blank=True, null=True)),
                ('ftp_limit', models.IntegerField(blank=True, null=True)),
                ('sql_limit', models.IntegerField(blank=True, null=True)),
                ('quota_sh_limit', models.IntegerField(blank=True, null=True)),
                ('quota_www_limit', models.IntegerField(blank=True, null=True)),
                ('quota_mail_limit', models.IntegerField(blank=True, null=True)),
                ('quota_ftp_limit', models.IntegerField(blank=True, null=True)),
                ('quota_sql_limit', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('uprate_n', models.IntegerField(blank=True, null=True)),
                ('upceil_n', models.IntegerField(blank=True, null=True)),
                ('downrate_n', models.IntegerField(blank=True, null=True)),
                ('downceil_n', models.IntegerField(blank=True, null=True)),
                ('climit_n', models.IntegerField(blank=True, null=True)),
                ('plimit_n', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tariffs',
                'managed': False,
            },
        ),
    ]
