# Generated by Django 4.2.2 on 2023-10-18 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='manufacture',
            new_name='manufacturer',
        ),
    ]
