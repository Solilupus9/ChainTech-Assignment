# Generated by Django 5.0.1 on 2024-02-03 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0004_alter_data_age_alter_data_pno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='Email',
            new_name='Email_ID',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='Fname',
            new_name='First_Name',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='Lname',
            new_name='Last_Name',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='pw',
            new_name='Password',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='Pno',
            new_name='Phone_Number',
        ),
    ]