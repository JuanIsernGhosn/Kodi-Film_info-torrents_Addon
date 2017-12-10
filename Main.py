# -*- coding: utf-8 -*-

from ClientTools import getSoup
from filmaffinity.filmaffinity import find_films
from filmaffinity.filmaffinity import get_film_page


for film in find_films('Tom Hanks',True):
    print(get_film_page(film[3])['actors'])


