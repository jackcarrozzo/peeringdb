# Generated by Django 4.2.10 on 2024-02-19 13:48

import django_peeringdb.fields
import django_peeringdb.models.abstract
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0122_fix_voltage"),
    ]

    operations = [
        migrations.AddField(
            model_name="facility",
            name="notified_for_geocoords",
            field=models.BooleanField(
                default=False,
                help_text="Indicates whether the facility has been notified to update their geocoordinates.",
            ),
        ),
    ]