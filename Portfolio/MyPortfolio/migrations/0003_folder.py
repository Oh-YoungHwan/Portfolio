# Generated by Django 4.2.7 on 2024-01-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MyPortfolio", "0002_robotstxt"),
    ]

    operations = [
        migrations.CreateModel(
            name="Folder",
            fields=[
                (
                    "id",
                    models.AutoField(db_column="ID", primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=25)),
                ("address", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "folder",
                "managed": False,
            },
        ),
    ]
