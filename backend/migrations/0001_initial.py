# Generated by Django 3.2.8 on 2021-10-27 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('pair', models.CharField(choices=[('BRLBTC', 'BRLBTC'), ('BRLETH', 'BRLETH')], max_length=10, verbose_name='PAIR')),
                ('timestamp', models.BigIntegerField()),
                ('mms_20', models.FloatField()),
                ('mms_50', models.FloatField()),
                ('mms_200', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
