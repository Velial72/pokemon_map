from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    text = models.TextField()