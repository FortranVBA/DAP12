# Generated by Django 3.2.6 on 2021-09-01 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('contract', '0002_rename_client_contract_clientid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='ClientID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client'),
        ),
    ]