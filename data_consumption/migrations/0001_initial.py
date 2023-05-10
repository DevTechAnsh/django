# Generated by Django 4.1.3 on 2022-12-02 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BuildingData",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("name", models.CharField(max_length=255, null=True)),
            ],
            options={
                "db_table": "building_data",
            },
        ),
        migrations.CreateModel(
            name="MeterData",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("fuel", models.CharField(max_length=255, null=True)),
                ("unit", models.CharField(max_length=20, null=True)),
                (
                    "building",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data_consumption.buildingdata",
                    ),
                ),
            ],
            options={
                "db_table": "meter_data",
            },
        ),
        migrations.CreateModel(
            name="HalfHourlyData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("consumption", models.FloatField(null=True)),
                ("reading_date_time", models.DateTimeField()),
                (
                    "meter",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data_consumption.meterdata",
                    ),
                ),
            ],
            options={
                "db_table": "half_hourly_data",
            },
        ),
    ]
