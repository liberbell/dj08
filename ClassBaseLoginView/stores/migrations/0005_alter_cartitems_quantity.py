# Generated by Django 4.2.2 on 2023-10-28 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_addresses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
