# Generated by Django 4.2.5 on 2023-11-22 21:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("master", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="governorate",
            name="area",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="governorate",
            name="centers",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="governorate",
            name="cities",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="governorate",
            name="main_city",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="governorate",
            name="neighborhoods",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="governorate",
            name="population",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="department",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="governorate",
            name="discription",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="governorate",
            name="latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="governorate",
            name="longitude",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
