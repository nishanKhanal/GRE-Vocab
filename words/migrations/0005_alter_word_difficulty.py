# Generated by Django 3.2.7 on 2021-09-27 17:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0004_auto_20210927_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='difficulty',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
