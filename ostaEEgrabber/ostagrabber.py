"""Data grabber for 'Osta.ee'."""


from bs4 import BeautifulSoup
import requests
import json  # For dumping to json file.


# Divided address to switch faster between categories, if needed.
main = 'https://www.osta.ee/'
category = 'kategooria/arvutid'

# Initial URL.
start_url = f'{main}{category}'
# List of grabbed dictionaries.
database = []


def parser(start_url):
    """
    Grabs listing of items for available for sale in specified category.

    By default the category is "Arvutid".

    Parameters
    ----------
    start_url : url of web page from which starts grabbing.

    Returns
    -------
    "osta.json" file with grabbed Title, Price and link to the picture of item.

    """
    page = requests.get(start_url)
    soup = BeautifulSoup(page.text, 'html.parser')

    bricks_list = soup.find_all('li', class_='col-md-4 mb-30')

    # Picking required data.
    for brick in bricks_list:
        data = {'Title': '', 'Price': '', 'Picture href': ''}
        data['Title'] = brick.p.get_text(' ', strip=True)
        for price in brick.find_all('span', class_=lambda name:
                                    name == 'price-bn price-cp'):
            data['Price'] = price.get_text(' ', strip=True)
        data['Picture href'] = brick.a.img['data-original']
        database.append(data)

    # Writing data to json file. Each listing from new line.
    with open("osta.json", "w", encoding='utf-8') as output:
        for data in database:
            json.dump(data, output, ensure_ascii=False)
            output.write('\n')

    # Checking, if there are more pages in this category and parsing next page.
    try:
        next_page = soup.find('a', class_='icon next page-link')['href']
        if next_page:
            page_url = f'{main}{next_page}'
            parser(page_url)
    except KeyError:
        print("All data saved. No more pages left.")


parser(start_url)
