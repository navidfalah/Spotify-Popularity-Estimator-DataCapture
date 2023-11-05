# Generated by Django 4.2.6 on 2023-11-04 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("spotifier", "0016_artist_main_artist"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trackclone",
            name="artists",
        ),
        migrations.AddField(
            model_name="trackclone",
            name="artist",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="spotifier.artist",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="trackclone",
            name="artists_list",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]