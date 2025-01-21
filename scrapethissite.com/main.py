import requests
from bs4 import BeautifulSoup
from pprint import pprint


base_url = 'https://www.scrapethissite.com/'
url = 'https://www.scrapethissite.com/pages/'
pages_dict = {}

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

div_tag = soup.find('div', class_='row')
pages = div_tag.find_all('div', class_='page')
for page in pages:
    a_tag_page_link = page.find('a')
    pages_dict[a_tag_page_link.text] = base_url + a_tag_page_link['href']