# Generated by Django 4.0.3 on 2022-03-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0016_alter_word_antonyms_alter_word_synonyms'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
