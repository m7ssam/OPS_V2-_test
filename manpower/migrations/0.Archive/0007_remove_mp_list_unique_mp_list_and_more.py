# Generated by Django 4.2.5 on 2023-11-19 17:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("manpower", "0006_alter_mp_list_recipient_mp_location"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="mp_list",
            name="unique_mp_list",
        ),
        migrations.RemoveField(
            model_name="historicalmp_list",
            name="recipient",
        ),
        migrations.RemoveField(
            model_name="mp_list",
            name="recipient",
        ),
    ]