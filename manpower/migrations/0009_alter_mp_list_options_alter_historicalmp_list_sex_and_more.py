# Generated by Django 4.2.5 on 2023-11-26 16:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manpower", "0008_alter_mp_list_photo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mp_list",
            options={"ordering": ["id"]},
        ),
        migrations.AlterField(
            model_name="historicalmp_list",
            name="sex",
            field=models.CharField(
                choices=[("male", "male"), ("female", "female")], max_length=10
            ),
        ),
        migrations.AlterField(
            model_name="mp_list",
            name="sex",
            field=models.CharField(
                choices=[("male", "male"), ("female", "female")], max_length=10
            ),
        ),
    ]
