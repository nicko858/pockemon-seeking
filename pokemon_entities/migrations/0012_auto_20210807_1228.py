# Generated by Django 3.1.13 on 2021-08-07 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_auto_20210807_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(max_length=200, null=True, verbose_name='Японское название'),
        ),
    ]