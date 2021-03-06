# Generated by Django 2.2.5 on 2019-10-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0002_auto_20191009_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temp',
            name='data',
        ),
        migrations.RemoveField(
            model_name='temp',
            name='unit',
        ),
        migrations.AddField(
            model_name='temp',
            name='humidity',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='temp',
            name='moisture',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='temp',
            name='temperature',
            field=models.FloatField(default=-1.0),
        ),
    ]
