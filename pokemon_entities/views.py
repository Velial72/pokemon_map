import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.timezone import localtime
from pokemon_entities.models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)

def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)

def get_image_url(request, pokemon):
    img_url = DEFAULT_IMAGE_URL
    if pokemon.photo:
        img_url = request.build_absolute_uri(pokemon.photo.url)
    return img_url

def show_all_pokemons(request):
    now = localtime()
    pokemon_entities = PokemonEntity.objects.select_related('pokemon').exclude(
        appeared_at__gt=now).exclude(disappeared_at__lte=now)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            get_image_url(request, pokemon_entity.pokemon)
        )
    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': get_image_url(request, pokemon),
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    now = localtime()
    requested_pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    pokemon_entities = PokemonEntity.objects.select_related('pokemon').filter(pokemon=requested_pokemon).exclude(
        appeared_at__gt=now).exclude(disappeared_at__lte=now)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            get_image_url(request, pokemon_entity.pokemon)
        )
    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': get_image_url(request, pokemon),
            'title_ru': pokemon.title,
            'title_en': pokemon.title_en,
            'title_jp': pokemon.title_jp,
            'description': pokemon.description
        })

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': {
            'pokemon_id': pokemon.id,
            'img_url': requested_pokemon.photo.url,
            'title_ru': pokemon.title,
            'title_en': pokemon.title_en,
            'title_jp': pokemon.title_jp,
            'description': pokemon.description
        }
    })
