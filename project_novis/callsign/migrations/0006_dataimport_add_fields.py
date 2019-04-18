# Generated by Django 2.2 on 2019-04-18 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callsign', '0005_telco_import'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataimport',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dataimport',
            name='error_message',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='dataimport',
            name='failed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dataimport',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
