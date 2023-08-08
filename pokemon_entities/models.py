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
    appeared_at = models.DateTimeField(verbose_name='Появляется', null=True)
    disappeared_at = models.DateTimeField(verbose_name='Пропадает', null=True)
    level = models.IntegerField(verbose_name='Уровень', null=True)
    health = models.IntegerField(verbose_name='Здоровье', null=True)
    attack = models.IntegerField(verbose_name='Атака', null=True)
    defence = models.IntegerField(verbose_name='Защита', null=True)
    stamina = models.IntegerField(verbose_name='Выносливость', null=True)