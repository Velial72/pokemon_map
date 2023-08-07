from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    text = models.TextField()
    photo = models.ImageField(upload_to='pokemons', null=True)

    def __str__(self):
        return self.text