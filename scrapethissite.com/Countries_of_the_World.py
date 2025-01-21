import requests
from bs4 import BeautifulSoup
from main import pages_dict
from pprint import pprint


url = pages_dict['Countries of the World: A Simple Example']
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

countries_rows = soup.find_all('div', class_='row')
countries_rows = countries_rows[3:]
counter = 0

print(len(countries_rows))

for row in countries_rows:
    countries_in_row = row.find_all('div', class_='col-md-4 country')
    for country in countries_in_row:
        country_dictionary = {}
        country_info_mix = country.find('div', class_='country-info')
        country_atributes = country_info_mix.find_all('strong') # list in order capital, population, area
        
        country_name = country.find('h3', class_='country-name').text
        country_name = country_name.strip() # Deleting extra withespaces and
        country_capital = country_info_mix.find('span', class_='country-capital').text
        country_population = country_info_mix.find('span', class_='country-population').text
        country_area = country_info_mix.find('span', class_='country-area').text
        
        # Save in dictionary
        country_dictionary[country_atributes[0].text] = country_capital
        country_dictionary[country_atributes[1].text] = country_population
        country_dictionary[country_atributes[2].text] = country_area
        counter += 1
        
        with open('Countries_of_the_World.txt', 'a', encoding='utf-8') as file:
            file.write(f'{counter}. ')
            file.write(f'{country_name} \n')
            for key, value in country_dictionary.items():
                file.write(f'{key} {value} \n')
            file.write('\n')