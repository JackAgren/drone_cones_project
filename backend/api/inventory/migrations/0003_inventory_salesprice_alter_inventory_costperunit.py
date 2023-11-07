# Generated by Django 4.2.6 on 2023-11-06 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_inventory_id_inventory_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='salesPrice',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventory',
            name='costPerUnit',
            field=models.FloatField(),
        ),
    ]
