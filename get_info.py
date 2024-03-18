import requests 
from bs4 import BeautifulSoup


def recup_info(seismes):
    return seismes["mag"], seismes["geometry"].x,seismes["geometry"].y


def recup_date():
    url = 'page.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    date_1 = soup.find(id = 'date')
    date_2 = soup.find(id = 'date 2')
    return (str(date_1), str(date_2))
