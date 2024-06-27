#First import essential libraries
import bs4
#BeautifulSoup4 for parsing HTML structures
from bs4 import BeautifulSoup

#requests for fetching web content
import requests

#Pandas for data analysis and manipulation
import pandas as pd

#CSV for creating CSV files
import csv

URL = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

req = requests.get(URL)

req.status_code

soup = bs4.BeautifulSoup(req.text, 'html.parser')

table = soup.findAll('table')[0]
rows = table.findAll('tr')

for row in rows[0:]:
    cells = row.findAll('td')
    UPC = cells[0].text.strip()
    print(UPC)
