# Generated by Django 5.0.1 on 2024-02-03 10:35

import Project.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0005_rename_email_data_email_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Phone_Number',
            field=models.IntegerField(validators=[Project.models.valid_pno]),
        ),
    ]