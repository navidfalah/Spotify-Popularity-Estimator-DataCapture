# Generated by Django 4.2.6 on 2023-10-15 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotifier', '0007_track_created_track_modified_track_release_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='release_date',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
