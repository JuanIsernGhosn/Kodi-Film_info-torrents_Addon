# -*- coding: utf-8 -*-

class Page(object):
    """This is a simple python scraping.

    Attributes:
        soup (TYPE): Page analyzed by BeautifulSoup.
    """

    def __init__(self, soup):
        """Init the class.

        Args:
            soup (TYPE): Page analyzed by BeautifulSoup
        """
        self.soup = soup

    def getTitle(self):
        """Get title."""
        title = self.soup.find('h1', {'id': 'main-title'}).find('span', {'itemprop': 'name'})
        return title.get_text() if title else None

    def getOriginalTitle(self):
        """Get title."""
        title = self.soup.find('div', {'id': 'left-column'}).find('dd')
        return title.get_text().strip() if title else None

    def getRunningTime(self):
        """Get title."""
        title = self.soup.find('dd', {'itemprop': 'duration'})
        return title.get_text() if title else None

    def getSynopsis(self):
        synopsis = self.soup.find('dd', {'itemprop': 'description'})
        return synopsis.get_text().strip() if synopsis else None

    def getRating(self):
        """Get rating."""
        rating = self.soup.find("div", {"id": 'movie-rat-avg'})
        if rating:
            try:
                rating = float(rating.get_text())
            except ValueError:
                rating = rating.get_text().strip()
        return rating

    def getDirectors(self):
        """Get directors."""
        directors = {}
        directorCell = self.soup.find_all('span', {'itemprop': 'director'})
        if directorCell:
            for director in directorCell:
                directors[director.find('span', {'itemprop': 'name'}).getText()] = director.find('a', {'itemprop': 'url'})['href']
        return directors if directors else None

    def getActors(self):
        """Get directors."""
        actors = {}
        actorCell = self.soup.find_all('span', {'itemprop': 'actor'})
        if actorCell:
            for actor in actorCell:
                actors[actor.find('span', {'itemprop': 'name'}).getText()] = actor.find('a', {'itemprop': 'url'})['href']
        return actors if actors else None

    def getPoster(self):
        """Get poster."""
        poster_img = None
        poster = self.soup.find('div', {'id': 'movie-main-image-container'})
        if poster:
            poster_img = poster.find('img')
            poster_img = poster_img['src']
        return poster_img
