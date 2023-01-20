# Generated by Django 4.1.4 on 2023-01-20 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manageApp", "0007_alter_student_roll_number"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
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
                ("Depart_Name", models.CharField(max_length=40)),
                ("HeadOfDepart", models.CharField(max_length=40)),
                ("Total_Faculty", models.CharField(max_length=10)),
            ],
            options={"db_table": "department",},
        ),
        migrations.CreateModel(
            name="Event",
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
                ("Event_Name", models.CharField(max_length=40)),
                ("Event_Date", models.DateField(default="2022-11-21")),
                ("Event_Time", models.CharField(max_length=10)),
                ("Chief_Guest", models.CharField(max_length=10)),
            ],
            options={"db_table": "event",},
        ),
    ]