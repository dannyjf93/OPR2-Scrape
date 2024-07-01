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

soup = bs4.BeautifulSoup(req.text, 'html.parser')
table = soup.find('table', class_='table-striped')
headers = table.findAll('th')
product_info = table.findAll('td')

#Create variables for information needed
bs_descriptions = soup.findAll('p')
description = bs_descriptions[3].string
product_headers = headers[0:6]
product_data = product_info[0:6]
bs_titles = soup.findAll('h1')
title = bs_titles[0].string
bs_categories = soup.find_all('a')
category = bs_categories[3].string
#How can I get the actual class (star-rating.Three) displayed as just the text of the class
review_rating = bs_descriptions[2].string
image_tag = soup.findAll('img')
image_url = [img['src'] for img in image_tag]

#Create lists to be called in dataframe
Column_1 = ['Product Page URL', 'UPC', 'Book Title', 'Price Including Tax', 'Price Excluding Tax', 'Quantity Available', 'Product Description', 'Category', 'Review Rating', 'Image URL']
Column_2 = [URL, product_data[0].string, title, product_data[3].string, product_data[2].string, product_data[5].string, bs_descriptions[3].string, category, review_rating, image_url]

#create dataframe
bookInformation = pd.DataFrame({'Book Information': Column_1,
                                'Book Data': Column_2})

df = pd.DataFrame(bookInformation)

#Export dataframe as CSV
book_csv_data = df.to_csv('bookData.csv', index=True)

print('\nCSV String:\n', book_csv_data)