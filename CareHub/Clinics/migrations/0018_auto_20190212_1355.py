# Generated by Django 2.1.2 on 2019-02-12 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clinics', '0017_auto_20190212_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='timeSlotss',
            new_name='timeSlots',
        ),
    ]
