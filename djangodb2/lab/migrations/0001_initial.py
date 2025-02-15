# Generated by Django 5.1.2 on 2024-10-25 08:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('license_plate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('contact_info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='lab.servicestation')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('order_status', models.CharField(max_length=50)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='lab.car')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='lab.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='lab.user')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='lab.user'),
        ),
    ]
