# Generated by Django 3.1.6 on 2021-05-02 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domain',
            old_name='last_scan_date',
            new_name='start_scan_date',
        ),
    ]
