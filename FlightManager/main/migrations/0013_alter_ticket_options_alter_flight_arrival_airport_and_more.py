# Generated by Django 4.0.4 on 2022-06-12 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_flightdetail_first_class_ticket_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_airport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arrival_airport', to='main.airport'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_airport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departure_airport', to='main.airport'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.customer'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='flight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.flight'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.ticketclass'),
        ),
        migrations.AlterField(
            model_name='transitionairport',
            name='airport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.airport'),
        ),
        migrations.AlterField(
            model_name='transitionairport',
            name='flight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.flight'),
        ),
    ]
