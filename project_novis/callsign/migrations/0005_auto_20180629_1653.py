# Generated by Django 2.1b1 on 2018-06-29 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callsign', '0004_prefix_import'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ESQLUser',
            new_name='EQSLUser',
        ),
    ]