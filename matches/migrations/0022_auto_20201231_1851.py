# Generated by Django 3.1 on 2020-12-31 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20201229_2156'),
        ('matches', '0021_auto_20201227_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='status',
            field=models.CharField(choices=[('C', 'Completed'), ('SF', 'Single Forfeit'), ('DF', 'Double Forfeit')], default='C', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='result',
            name='loser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lost_match_results', to='teams.team'),
        ),
        migrations.AlterField(
            model_name='result',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='won_match_results', to='teams.team'),
        ),
    ]
