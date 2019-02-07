# Generated by Django 2.1.2 on 2019-02-07 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clinics', '0002_auto_20190206_1656'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clinics.Service')),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='reservations',
            name='Clinic',
        ),
        migrations.RemoveField(
            model_name='reservations',
            name='Patient',
        ),
        migrations.DeleteModel(
            name='Reservations',
        ),
    ]
