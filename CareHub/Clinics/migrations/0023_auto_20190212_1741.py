# Generated by Django 2.1.2 on 2019-02-12 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clinics', '0022_auto_20190212_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='OpenSlots',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Clinics.TimeSlots'),
        ),
    ]
