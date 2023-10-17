# Generated by Django 4.2.2 on 2023-10-17 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'manufacturers',
            },
        ),
        migrations.CreateModel(
            name='ProductTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'product_types',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('manufacture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.manufacturers')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.producttypes')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductPictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='product_pictures/')),
                ('order', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.products')),
            ],
            options={
                'db_table': 'product_pictures',
                'ordering': ['order'],
            },
        ),
    ]
