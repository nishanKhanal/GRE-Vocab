# Generated by Django 3.2.7 on 2021-09-28 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0005_alter_word_difficulty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ('difficulty', '-updated_at')},
        ),
        migrations.AddField(
            model_name='word',
            name='favourite',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='word',
            name='part_of_speech',
            field=models.CharField(default='noun', max_length=25),
            preserve_default=False,
        ),
    ]
