# Generated by Django 2.1.2 on 2019-02-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinics', '0008_reservation_dateofbook101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='DateOfBook101',
            field=models.DateField(),
        ),
    ]
