# Generated by Django 4.2.5 on 2023-11-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_id",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
