from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.TextField(verbose_name='Название')
    title_en = models.TextField(verbose_name='Название на английском', blank=True)
    title_jp = models.TextField(verbose_name='Название на японском', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
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
    lat = models.FloatField(verbose_name='Широта', null=True)
    lon = models.FloatField(verbose_name='Долгота', null=True)
    appeared_at = models.DateTimeField(verbose_name='Появляется', null=True)
    disappeared_at = models.DateTimeField(verbose_name='Пропадает', null=True)
    level = models.IntegerField(verbose_name='Уровень', null=True)
    health = models.IntegerField(verbose_name='Здоровье', blank=True)
    attack = models.IntegerField(verbose_name='Атака', blank=True)
    defence = models.IntegerField(verbose_name='Защита', blank=True)
    stamina = models.IntegerField(verbose_name='Выносливость', blank=True)

    def __str__(self):
        return f"{self.pokemon} Широта: {self.lat} Долгота: {self.lon}"
