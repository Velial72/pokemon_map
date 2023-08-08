from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    text = models.TextField()
    photo = models.ImageField(upload_to='pokemons', null=True)

    def __str__(self):
        return self.text

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', related_name='entities', on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Появляется')
    disappeared_at = models.DateTimeField(verbose_name='Пропадает')
    level = models.IntegerField(verbose_name='Уровень')
    health = models.IntegerField(verbose_name='Здоровье')
    attack = models.IntegerField(verbose_name='Атака')
    defence = models.IntegerField(verbose_name='Защита')
    stamina = models.IntegerField(verbose_name='Выносливость')