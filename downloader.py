import requests
from bs4 import BeautifulSoup

URL = "https://alermipianovendite.it/asta-alloggi-9-marzo-2023/"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
r = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')

table = soup.find('tbody', attrs={'class': 'row-hover'})

date = '20230309/'

for row in table.findAll('tr'):
    try:
        address = row.find('td', attrs={'class': 'column-4'}).text
    except:
        continue
    try:
        planimetry_link = row.find('td', attrs={'class': 'column-4'}).a['href']
        lotto = planimetry_link.split('planimetrie/')[1].split('.pdf')[0]
        pdf_response = requests.get(planimetry_link)
        file = open(date+lotto+'_planimetry.pdf', "wb")
        file.write(pdf_response.content)
        file.close()
    except:
        continue

    try:
        pictures_link = row.find('td', attrs={'class': 'column-13'}).a['href']

        pdf_response = requests.get(pictures_link)
        file = open(date+lotto+'_pictures.pdf', "wb")
        file.write(pdf_response.content)
        file.close()
    except:
        continue
