# Generated by Django 4.2.6 on 2023-11-12 19:38

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drone_operator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cone', models.CharField(max_length=25)),
                ('iceCream', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=25), size=None)),
                ('toppings', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=25), size=None)),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cones', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('location', models.CharField(max_length=200)),
                ('timeOrdered', models.DateTimeField()),
                ('timeDelivered', models.DateTimeField(null=True)),
                ('total', models.IntegerField()),
                ('droneID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone_operator.droneinfo')),
            ],
        ),
    ]