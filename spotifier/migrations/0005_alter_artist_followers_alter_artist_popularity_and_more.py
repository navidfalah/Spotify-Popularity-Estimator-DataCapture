# Generated by Django 4.2.5 on 2023-10-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotifier', '0004_alter_track_duration_ms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artist',
            name='popularity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='track',
            name='popularity',
            field=models.IntegerField(default=0),
        ),
    ]
