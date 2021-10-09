# Generated by Django 3.2.7 on 2021-09-27 16:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_auto_20210927_1244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ('-updated_at',)},
        ),
        migrations.AddField(
            model_name='word',
            name='difficulty',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
    ]
