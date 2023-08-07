from django.contrib import admin
from .models import Pokemon, PokemonEntity

admin.site.register(Pokemon)

class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(PokemonEntity)
