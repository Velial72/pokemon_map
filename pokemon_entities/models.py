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