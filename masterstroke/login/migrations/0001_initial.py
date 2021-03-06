# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-08 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(max_length=500)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('schoolNearby', models.CharField(max_length=100)),
                ('gardenNearby', models.CharField(max_length=100)),
                ('marketNearby', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(max_length=20)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='homedetails',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
    ]
