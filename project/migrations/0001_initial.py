# Generated by Django 4.2.5 on 2023-11-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Name",
            fields=[
                (
                    "recipient",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("project_name", models.CharField(max_length=50)),
            ],
        ),
    ]
