# Generated by Django 4.2.6 on 2023-10-14 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotifier', '0005_alter_artist_followers_alter_artist_popularity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='is_local',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='track',
            name='is_playable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='track',
            name='track_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
