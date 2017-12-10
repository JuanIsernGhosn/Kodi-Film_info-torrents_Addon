from ClientTools import getSoup
from filmaffinity.InfoboxFilmParser import Page
import urllib

base_url = "https://www.filmaffinity.com"

def find_films(data, by_cast=False):
    url = base_url+'/es/search.php?'
    films = []

    if by_cast:
        url = url+'stype=cast'
    else:
        url = url+'stype=title'

    url = url+'&stext='+urllib.parse.quote(data)
    soup = getSoup(url)

    if soup:
        film_cell = soup.find_all('div', {'class': 'se-it'})
        for film in film_cell:

            year=film.find('div', {'class': 'ye-w'})
            if year:
                year = year.getText()

            title=film.find('div', {'class': 'mc-title'}).find('a')
            if title:
                title = title.getText()

            poster=film.find('div', {'class': 'mc-poster'}).find('img')['src']

            url=film.find('div', {'class': 'mc-poster'}).find('a')['href']

            director=film.find('div', {'class': 'mc-director'}).find('a')
            if director:
                director = director.getText();

            films.append([year,title,director,url,poster])

    return films


def get_film_page(data):
    film={}
    url = base_url+data
    soup = getSoup(url)
    if soup:
        page = Page(soup)
        film['title'] = page.getTitle()
        film['originalTittle'] = page.getOriginalTitle()
        film['directors'] = page.getDirectors()
        film['actors'] = page.getActors()
        film['duration'] = page.getRunningTime()
        film['synopsis'] = page.getSynopsis()
        film['rating'] = page.getRating()
        film['poster'] = page.getPoster()
    return film
