# Generated by Django 5.1.4 on 2025-01-19 19:00

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pushuplog", "0005_alter_pushuplogentry_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="pushuplogentry",
            name="repetitions_total",
            field=models.GeneratedField(
                db_persist=True,
                expression=django.db.models.expressions.CombinedExpression(
                    models.F("sets"), "*", models.F("repetitions")
                ),
                output_field=models.SmallIntegerField(),
            ),
        ),
    ]
