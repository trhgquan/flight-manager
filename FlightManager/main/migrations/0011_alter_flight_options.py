# Generated by Django 4.0.3 on 2022-06-02 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_flight_transition_airports_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flight',
            options={'ordering': ('date_time',)},
        ),
    ]
