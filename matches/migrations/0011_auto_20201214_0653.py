# Generated by Django 3.1 on 2020-12-14 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0010_auto_20201214_0637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='sets',
        ),
        migrations.RemoveField(
            model_name='set',
            name='games',
        ),
        migrations.AddField(
            model_name='game',
            name='set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games', to='matches.set'),
        ),
        migrations.AddField(
            model_name='set',
            name='result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='selts', to='matches.result'),
        ),
    ]
