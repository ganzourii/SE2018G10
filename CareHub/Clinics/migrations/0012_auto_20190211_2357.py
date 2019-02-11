# Generated by Django 2.1.2 on 2019-02-11 21:57

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clinics', '0011_auto_20190211_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='Booker',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]