import requests
from bs4 import BeautifulSoup
import lxml
from pprint import pprint


counter = 0
for page in range(1, 11):
    base_url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    
    def tags_string(tags_list: list) -> str:
        ans = ''
        for tag in tags_list:
            if tag == tags_list[-1]:
                ans += f'{tag}'
                break
            ans += f'{tag}, '
        return ans

    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        counter +=1
        tags_list = []
        quote_text = quote.find('span', class_='text').text
        quote_author = quote.find('small', class_='author').text
        tags_div = quote.find('div', class_='tags')
        tags = tags_div.find_all('a', class_='tag')
        for tag in tags:
            tags_list.append(tag.text)
        with open('quotes_collector.txt', 'a', encoding='utf-8') as file:
            file.write(f'{counter}. ')
            file.write(f'Author: {quote_author} \n')
            file.write(f'Quote: {quote_text} \n')
            file.writelines(f'Tags: {tags_string(tags_list)} \n')
            file.write('\n')
        
             