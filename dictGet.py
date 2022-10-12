import requests
from bs4 import BeautifulSoup


def get(query):
    link = f"https://ordnet.dk/ddo/ordbog?query={query}"
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")
    deffRaw = soup.find_all("span", class_="definition")
    deffPure = [i.text for i in deffRaw]
    wordRaw = soup.find_all("span", class_="match")
    wordPure = wordRaw[0].text
    word = {"word": wordPure, "deff": deffPure}
    return word
