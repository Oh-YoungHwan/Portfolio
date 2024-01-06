# Generated by Django 4.2.7 on 2024-01-06 02:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MyPortfolio", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RobotsTxt",
            fields=[
                (
                    "id",
                    models.AutoField(db_column="ID", primary_key=True, serialize=False),
                ),
                ("user_agent", models.CharField(db_column="User_agent", max_length=25)),
                ("disallow", models.CharField(db_column="Disallow", max_length=200)),
            ],
            options={
                "db_table": "robots_txt",
                "managed": False,
            },
        ),
    ]
