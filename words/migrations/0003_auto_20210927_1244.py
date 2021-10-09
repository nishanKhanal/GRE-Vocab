# Generated by Django 3.2.7 on 2021-09-27 12:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_auto_20210927_0358'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='word',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
