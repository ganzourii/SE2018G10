# Generated by Django 2.1.2 on 2019-02-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0006_doctor_clinic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='clinic',
        ),
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(height_field=300, null=True, upload_to=None, width_field=300),
        ),
    ]