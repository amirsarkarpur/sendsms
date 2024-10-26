# Generated by Django 5.0.6 on 2024-10-26 17:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='give_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('phone_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^09\\d{9}$', 'شماره موبایل باید با 09 شروع شود و 11 رقم باشد.')])),
            ],
        ),
    ]
