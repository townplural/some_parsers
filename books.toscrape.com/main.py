import requests
import re
from pprint import pprint
from bs4 import BeautifulSoup
from check import check_connection

if check_connection():
    base_url = "https://books.toscrape.com/catalogue/"
    all_books_info = []


    def new_get_soup(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        return soup

    def correct_description(text:str) -> str:
        text.replace('<p>', '')
        # TODO translation description and return translated discription
        return text


    def get_price(soup) -> str:
        price = soup.find('p', class_='price_color').text
        fixed_price = price.encode('latin1').decode('utf-8')
        return fixed_price
        

    def get_stock_availability(soup) -> int:
        stock_availability = ''
        availability_text = soup.find('p', class_='instock availability').text
        pattern = r"\d"
        match = re.findall(pattern, availability_text)
        if len(match) > 1: 
            for i in match:
                stock_availability += i
        else:
            stock_availability += match[0]
        return int(stock_availability)
            
        
    def get_max_page():
        url = "https://books.toscrape.com/index.html"
        pattern = r"\d{2}"
        pages = new_get_soup(url)
        page_counter = pages.find('li', class_='current')
        match = re.search(pattern, page_counter.text)
        max_page = match.group()
        return int(max_page)


    counter = 0
    for i in range(1, get_max_page() + 1):
        page_soup = new_get_soup(url=base_url + f"page-{i}.html")
        books_list = page_soup.find_all('article', class_='product_pod')


        for book in books_list:
            data = {}
            
            # get book in-built link
            image_container = book.find('div', class_='image_container')
            tag_a = image_container.find('a')
            book_link = tag_a['href']
            data["Link"] = base_url + book_link
            
            # Book page soup
            book_page_soup = new_get_soup(data["Link"])
            book_page_article = book_page_soup.find('article', class_='product_page')
            book_div = book_page_article.find('div', class_='row')
            book_div_2 = book_div.find('div', class_='col-sm-6 product_main')
            
            # Book description after first book broken -_- (probably can add search for "...more"(in every description(not sure)))
            description_tag_p = book_page_article.find_all('p')
            pprint(description_tag_p)
            print(description_tag_p[-1].text)
            description = description_tag_p[-1].text
            
            # Title
            book_name = book_div_2.find('h1').text
            # images = book_div_2.find_all('img')
            
            # Saving all data
            data["Title"] = book_name
            data["Price"] = get_price(book_div_2)        
            data["In stock"] = get_stock_availability(book_div_2)
            data["Availability"] = True
            # data["Description"] = correct_description(description)
            
            # pprint(data)
            counter += 1
            print(f"{counter}: {data}")
    print(counter)
            