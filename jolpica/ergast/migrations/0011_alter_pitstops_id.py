# Generated by Django 3.2.6 on 2021-08-08 09:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ergast", "0010_auto_20210808_1052"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pitstops",
            name="id",
            field=models.CharField(
                max_length=255, primary_key=True, serialize=False, verbose_name="Unique id '<raceId>|<driverId>|<stop>'"
            ),
        ),
    ]
