# Generated by Django 4.0.3 on 2022-04-14 03:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_alter_post_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('detail', models.TextField(max_length=200)),
                ('date', models.DateField()),
                ('ex_date', models.DateTimeField()),
                ('price', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='ticket_pic')),
                ('sale', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.profile')),
            ],
        ),
    ]