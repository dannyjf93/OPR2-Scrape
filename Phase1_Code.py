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
    cells = row.findAll('th')
    UPC = cells[0].text.strip()
    Product_Type = cells[1].text.strip()
    Price_Excluding_Tax = cells[2].text.strip()
    Price_Including_Tax = cells[3].text.strip()
    Tax = cells[4].text.strip()
    Availability = cells[5].text.strip()
    Number_of_Reviews = cells[6].text.strip()
    print(UPC, Product_Type, Price_Excluding_Tax, Price_Including_Tax, Tax, Availability, Number_of_Reviews)
    print()

HEADERS = [
    'product_page_url',
    'universal_product_code',
    'book_title',
    'price_including_tax',
    'price_excluding_tax',
    'quantity_available',
    'product description',
    'category',
    'review_rating',
    'image_url'
]