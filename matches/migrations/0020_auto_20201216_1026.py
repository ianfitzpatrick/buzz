# Generated by Django 3.1 on 2020-12-16 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casters', '0007_auto_20201216_1020'),
        ('matches', '0019_auto_20201216_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='primary_caster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='casted_matches', to='casters.caster'),
        ),
    ]
