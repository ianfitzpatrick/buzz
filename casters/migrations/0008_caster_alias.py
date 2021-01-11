# Generated by Django 3.1 on 2021-01-11 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0010_auto_20210109_2253'),
        ('casters', '0007_auto_20201216_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='caster',
            name='alias',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='casters', to='players.alias'),
        ),
    ]
