# Generated by Django 2.1.2 on 2019-02-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0004_auto_20190206_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(blank=True, max_length=70, unique=True),
        ),
    ]
