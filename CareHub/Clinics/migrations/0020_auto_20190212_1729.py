# Generated by Django 2.1.2 on 2019-02-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinics', '0019_auto_20190212_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslots',
            name='t_id',
        ),
        migrations.AddField(
            model_name='timeslots',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
