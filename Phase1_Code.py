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
table = soup.find('table', class_='table-striped')
headers = table.findAll('th')
product_data = table.findAll('td')

#how do I get the actual text from this portion of the product page if the paragraph is separated from the ID/Class?
product_description = soup.findAll('p', class_='sub-header')

print(headers, product_data)

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