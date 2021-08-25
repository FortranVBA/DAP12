# Generated by Django 3.2.6 on 2021-08-25 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210825_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='StaffProfileID',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='account.staffprofile'),
        ),
    ]
