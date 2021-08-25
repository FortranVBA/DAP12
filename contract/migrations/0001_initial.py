# Generated by Django 3.2.6 on 2021-08-25 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractStatut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateCreated', models.DateTimeField(auto_now_add=True)),
                ('DateUpdated', models.DateTimeField(auto_now=True)),
                ('Amount', models.FloatField()),
                ('PaymentDue', models.DateTimeField()),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ContractStatutID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.contractstatut')),
            ],
        ),
    ]
