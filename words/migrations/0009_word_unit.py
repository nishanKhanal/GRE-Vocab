# Generated by Django 3.2.7 on 2021-09-29 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0008_word_terms_from_arts_sciences_and_social_sciences'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='unit',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
