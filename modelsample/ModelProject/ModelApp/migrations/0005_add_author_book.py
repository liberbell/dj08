# Generated by Django 4.2.2 on 2023-07-24 23:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelApp', '0004_add_place_restaurants'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 24, 23, 35, 6, 69176, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 24, 23, 35, 6, 69208, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('authors', models.ManyToManyField(to='ModelApp.authors')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
