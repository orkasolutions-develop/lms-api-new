# Generated by Django 3.0.9 on 2020-08-04 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rbbackup', '0003_routers_isactivated'),
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
    ]
