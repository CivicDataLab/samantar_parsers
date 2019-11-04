"""
Script for scraping Budget Speeches (India)

Usage:
    speech_scraper.py [--path=<p> --year=<y>]

Options:
    --path=<p>      Specify the path (Optional)
    --year=<y>      Specify the year (Optional)
"""
from docopt import docopt
from typing import List
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.indiabudget.gov.in/"


def construct_url():
    return BASE_URL + "bspeech.php"


def get_table():
    url = construct_url()
    page = requests.get(url)

    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find('table')
        return table
    return "page is not available!"


def save_file(content_url, path, filename):
    response = requests.get(content_url)
    filename = path + filename
    with open(filename + ".pdf", 'wb') as f:
        f.write(response.content)


if __name__ == "__main__":
    args = docopt(__doc__)
    path = args["--path"]
    year = args["--year"]

    table = get_table()

    for row in table.find_all('tr'):
        columns = row.find_all('td')
        for column in columns:
            try:
                url = column.find_all('a')[0]['href']
                if url.endswith('.pdf'):
                    name = column.find_all('a')[0].contents[0]
                    first_year = name.split('-')[0].strip()

                    filename = name.replace(' ', '_')
                    content_url = BASE_URL + url
                    if path:
                        if year and year == first_year:
                            save_file(content_url, path, filename)
                            quit()
                        if not year:
                            save_file(content_url, path, filename)

            except IndexError:
                pass
