# Generated by Django 3.0.5 on 2021-10-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0025_auto_20211020_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notices',
            name='description',
            field=models.TextField(),
        ),
    ]
