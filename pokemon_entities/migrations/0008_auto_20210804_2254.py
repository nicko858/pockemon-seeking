# Generated by Django 3.1.13 on 2021-08-04 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20210804_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='image',
            new_name='img_url',
        ),
    ]