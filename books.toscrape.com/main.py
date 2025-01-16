import requests
import re
from pprint import pprint
from bs4 import BeautifulSoup
from check import check_connection

if check_connection():
    



    base_url = "https://books.toscrape.com/catalogue/"


def get_soup():
    url = "https://books.toscrape.com/catalogue/page-1.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    return soup


def get_max_page():
    url = "https://books.toscrape.com/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")


    pages = get_soup().find('li', class_='current')
    pattern = r"\d{2}"
    match = re.search(pattern, pages.text)
    max_page = match.group()
    return int(max_page)



# page 
for i in range(1, get_max_page() + 1):
    page_response = requests.get(base_url + f"page-{i}.html")
    page_soup = BeautifulSoup(page_response.text, "lxml")
    books_list = page_soup.find_all('article', class_='product_pod')


    for book in books_list:
        data = {}
        # get book in-built link
        image_container = book.find('div', class_='image_container')
        tag_a = image_container.find('a')
        link = tag_a['href']
        data['Link'] = base_url + link

        book_response = requests.get(base_url + link)
        book_soup = BeautifulSoup(book_response.text, "lxml")

        # get book description
        book_body = book_soup.find('article', class_='product_pod')
        description = book_body.find('div', class_='product_description').text
        data['Description'] = description

        # get book name 
        









