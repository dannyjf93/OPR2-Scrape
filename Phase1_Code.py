#First import essential libraries

#BeautifulSoup4 for parsing HTML structures
from bs4 import BeautifulSoup

#requests for fetching web content
import requests

#Pandas for data analysis and manipulation
import pandas as pd

#CSV for creating CSV files
import csv

class BookScraper:
    def __init__(self):
        self.base_url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

    def scrape_book_details(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        book_details = []

        for book in soup.findAll('table', class_='table-striped'):
            product_page_url = book.h3.a.get('href')
            UPC = book.find('th', class_='UPC')
            book_title = book.find('hl', class_='col-sm-6 product_main')
            price_including_tax = book.find('th', class_='Price(incl. tax')
            price_excluding_tax = book.find('th', class_='Price(excl. tax')
            quantity_available = book.find('th', class_='Availability')
            product_description = book.find('p', class_='sub-header')
            category = book.find('li', class_='a href')
            review_rating = book.find('p', class_= 'star-rating')['class'][1]
            image_url = book.img.get('src')

            book_info = {
                'Product Page URL': product_page_url,
                'UPC': UPC,
                'Book Title': book_title,
                'Price Including Tax': price_including_tax,
                'Price Excluding Tax': price_excluding_tax,
                'Quantity Available': quantity_available,
                'Product Description': product_description,
                'Category': category,
                'Review Rating': review_rating,
                'Image URL': image_url
            }
            book_details.append(book_info)

        return book_details

