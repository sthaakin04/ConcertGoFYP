# Generated by Django 4.0.3 on 2022-04-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0016_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ex_date',
            field=models.DateField(),
        ),
    ]
