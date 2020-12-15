# Generated by Django 3.1 on 2020-12-15 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0004_auto_20201213_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='season',
            old_name='playoffs_end',
            new_name='tournament_end',
        ),
        migrations.RenameField(
            model_name='season',
            old_name='playoffs_start',
            new_name='tournament_start',
        ),
        migrations.AddField(
            model_name='season',
            name='num_regular_rounds',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='season',
            name='num_tournament_rounds',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.PositiveSmallIntegerField(default=1)),
                ('is_bracket', models.BooleanField(verbose_name=models.BooleanField(default=False))),
                ('circuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.circuit')),
            ],
        ),
    ]
