# Generated by Django 5.1.3 on 2025-01-17 22:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pushuplog", "0003_alter_pushuplogentry_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="pushuplogentry",
            name="when",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
