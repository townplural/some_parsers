import requests
from bs4 import BeautifulSoup

def check_connection():
    url = "https://books.toscrape.com/catalogue/page-1.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    if response.status_code == 200:
        return True
    return False