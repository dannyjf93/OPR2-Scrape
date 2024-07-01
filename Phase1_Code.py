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
product_info = table.findAll('td')

#how do I only pull the product description?
bs_descriptions = soup.findAll('p')
description = bs_descriptions[3].string
header = headers[0:6]
product_data = product_info[0:6]
bs_titles = soup.findAll('h1')
title = bs_titles[0].string
bs_categories = soup.find_all('a')
category = bs_categories[3].string
review_rating = bs_descriptions[2].string
image_url = soup.findAll('img')

print(bs_descriptions[3].string)
print(header[0].string, product_data[0].string)
print(title)
print(category)
print(review_rating)
print(image_url)