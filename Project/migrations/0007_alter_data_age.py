# Generated by Django 5.0.1 on 2024-02-03 10:36

import Project.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0006_alter_data_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Age',
            field=models.IntegerField(validators=[Project.models.valid_age]),
        ),
    ]
