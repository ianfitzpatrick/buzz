# Generated by Django 3.1 on 2021-03-01 09:32

from django.db import migrations, models
import teams.models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20210301_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='invite_code',
            field=models.CharField(blank=True, default=teams.models._generate_invite_code, max_length=8, unique=True),
        ),
    ]
