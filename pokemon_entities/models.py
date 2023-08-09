from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.TextField(verbose_name='Название')
    title_en = models.TextField(verbose_name='Название на английском')
    title_jp = models.TextField(verbose_name='Название на японском')
    description = models.TextField(verbose_name='Описание')
    next_evolution = models.ForeignKey("self",
                                       verbose_name='В кого эволюционирует',
                                       null=True,
                                       blank=True,
                                       related_name="previous_evolutions",
                                       on_delete=models.SET_NULL)
    photo = models.ImageField(upload_to='pokemons', null=True)

    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', related_name='entities', on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name='Широта', blank=True)
    lon = models.FloatField(verbose_name='Долгота', blank=True)
    appeared_at = models.DateTimeField(verbose_name='Появляется', blank=True)
    disappeared_at = models.DateTimeField(verbose_name='Пропадает', blank=True)
    level = models.IntegerField(verbose_name='Уровень', blank=True)
    health = models.IntegerField(verbose_name='Здоровье', blank=True)
    attack = models.IntegerField(verbose_name='Атака', blank=True)
    defence = models.IntegerField(verbose_name='Защита', blank=True)
    stamina = models.IntegerField(verbose_name='Выносливость', blank=True)

    def __str__(self):
        return f"{self.pokemon} Широта: {self.lat} Долгота: {self.lon}"