# Generated by Django 4.2.6 on 2023-11-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("spotifier", "0015_trackclone_downloaded"),
    ]

    operations = [
        migrations.AddField(
            model_name="artist",
            name="main_artist",
            field=models.BooleanField(default=False),
        ),
    ]
