# Generated by Django 4.0.3 on 2022-04-16 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0012_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
