# Generated by Django 3.2.6 on 2021-08-25 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='StaffProfileID',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='bio',
        ),
        migrations.DeleteModel(
            name='StaffProfile',
        ),
    ]
