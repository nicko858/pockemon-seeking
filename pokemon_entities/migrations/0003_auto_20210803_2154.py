# Generated by Django 3.1.13 on 2021-08-03 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_auto_20210803_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(),
        ),
    ]