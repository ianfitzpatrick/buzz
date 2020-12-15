# Generated by Django 3.1 on 2020-12-15 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0007_auto_20201215_2237'),
        ('matches', '0016_match_round'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='leagues.round'),
        ),
    ]
