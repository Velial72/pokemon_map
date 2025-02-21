# Generated by Django 3.1.14 on 2023-08-09 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20230809_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='attack',
            field=models.IntegerField(blank=True, verbose_name='Атака'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(blank=True, verbose_name='Защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(blank=True, verbose_name='Выносливость'),
        ),
    ]
