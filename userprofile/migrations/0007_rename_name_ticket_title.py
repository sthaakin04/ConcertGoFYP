# Generated by Django 4.0.3 on 2022-04-14 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_ticket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='name',
            new_name='title',
        ),
    ]
