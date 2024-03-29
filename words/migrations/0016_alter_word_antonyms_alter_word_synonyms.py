# Generated by Django 4.0.3 on 2022-03-17 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0015_auto_20211010_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='antonyms',
            field=models.ManyToManyField(blank=True, related_name='antomyms', to='words.word'),
        ),
        migrations.AlterField(
            model_name='word',
            name='synonyms',
            field=models.ManyToManyField(blank=True, related_name='synonyms', to='words.word'),
        ),
    ]
