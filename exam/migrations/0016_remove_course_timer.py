# Generated by Django 3.0.5 on 2021-10-19 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0015_auto_20211019_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='timer',
        ),
    ]
