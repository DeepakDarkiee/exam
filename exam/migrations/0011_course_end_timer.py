# Generated by Django 3.0.5 on 2021-10-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0010_auto_20211019_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='end_timer',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]