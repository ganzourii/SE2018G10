# Generated by Django 2.1.2 on 2019-02-06 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('expertise', models.CharField(max_length=50)),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('availability', models.BooleanField(default=False)),
            ],
        ),
    ]