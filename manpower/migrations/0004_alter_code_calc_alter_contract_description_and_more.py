# Generated by Django 4.2.5 on 2023-11-22 21:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manpower", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="code",
            name="calc",
            field=models.CharField(
                choices=[("direct", "direct"), ("indirect", "indirect")], max_length=10
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="job_type",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="title_list",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]