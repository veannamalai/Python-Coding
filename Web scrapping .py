
"""
Created on Sun May 13 17:32:26 2018
Web scrapping
@author: Anna
"""
from urllib.request import urlopen
import requests

webpage = requests.get("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India")
page = webpage.content

#print(page.read())

from bs4 import BeautifulSoup
soup = BeautifulSoup(page, 'html.parser')

all_links = soup.find_all("a")
for link in all_links:
    print (link.get("href"))
