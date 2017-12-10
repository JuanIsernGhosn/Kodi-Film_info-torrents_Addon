# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import requests

def getSoup(url):

    print(url)
    r = requests.get(url)
    status_code = r.status_code

    if status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")

    return soup if soup else None