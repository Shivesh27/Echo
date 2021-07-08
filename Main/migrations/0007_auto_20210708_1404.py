# Generated by Django 3.2.4 on 2021-07-08 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_auto_20210708_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingusers',
            name='contact',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='pendingusers',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
