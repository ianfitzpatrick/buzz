# Generated by Django 3.1 on 2020-12-14 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_player_twitch_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
