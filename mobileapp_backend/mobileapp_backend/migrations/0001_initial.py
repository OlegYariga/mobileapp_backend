# Generated by Django 3.0.6 on 2020-05-22 20:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeasTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Sets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('measdate', models.DateTimeField(default=datetime.datetime(2020, 5, 22, 23, 17, 15, 213881))),
                ('comment', models.CharField(max_length=600)),
                ('data', models.TextField()),
                ('setid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mobileapp_backend.Sets')),
                ('typeid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mobileapp_backend.MeasTypes')),
            ],
        ),
    ]
