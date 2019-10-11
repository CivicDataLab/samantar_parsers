from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

html = urlopen('https://www.indiabudget.gov.in/bspeech.php')
bs = BeautifulSoup(html, 'html.parser')
table = bs.find('table')

base_url = "https://www.indiabudget.gov.in/"
for row in table.find_all('tr'):
    column_marker = 0
    columns = row.find_all('td')
    for column in columns:
        url = column.find_all('a')[0]['href']
        if url.endswith('.pdf'):
            file = requests.get(base_url + url)
            bs_name = column.find_all('a')[0].contents[0].replace(' ', '_')
            with open("data/pdf/{}.pdf".format(bs_name), 'wb') as f:
                f.write(file.content)
