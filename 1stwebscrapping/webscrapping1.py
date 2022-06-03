#keytakeaways from this project:
#start small. Don't build the for loops first. build the details for each book first and then scale it. 
#this caused some small issues trying to test if I got the right data for each book.
#right now if I wanted to test something it would request the pages each time as I wanted to test. 

#TODO: Figure out why its not scrapping page 2 properly
#TODO: Figure out why it's not grabbing the next page
from random import betavariate
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import time

url = 'https://books.toscrape.com/'
r = requests.get(url).text
soup = BeautifulSoup(r)

#Find the total amount of pages
total_pages = soup.find('li', class_ = 'current').text
total_pages = int(total_pages.strip().split(' ')[-1])

#creating dictionary

data = {
    'Book Title': [],
    'Book Stars': [],
    'Book Price': [],
    'Book in Stock?': [],
    'Book URL': []
}

#figure out how to make it dynamic. Is there a constraint on a for loop maybe? Will the loop end after first page.
#maybe make 2 for loops. First is the page loop so it will loop through every page and then a 
#nested loop to look for the books?

for page in range(total_pages-1):
     books = soup.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
     for book in books:
         #Get details about each book
            book_title = str(book.find('h3')).split('"')
            book_title = book_title[3]

            book_stars = book.find('p', class_=re.compile('star-rating(.*)'))
            book_stars = str(book_stars).split('"')[1].replace('star-rating ', '')

            book_price = book.find('p', class_ = 'price_color').text
            book_price = float(book_price.replace('Â£', ''))

            book_stock = book.find('p', class_ = 'instock availability').text
            book_stock = book_stock.strip()
            if book_stock == 'In stock':
                book_stock = 'Y'
            else: 
                book_stock = 'N'

            book_url = str(book.find('h3')).split('"')
            book_url = url+book_url[1]
            data['Book Title'].append(book_title)
            data['Book Stars'].append(book_stars)
            data['Book Price'].append(book_price)
            data['Book in Stock?'].append(book_stock)
            data['Book URL'].append(book_url)
    #find the link to the next page to scrape all the pages.
     next_page = soup.find('li', class_='next').find('a')['href'].replace('catalogue/', '')
     url = 'https://books.toscrape.com/catalogue/'
     next_page = url+next_page
     print(next_page)
     #next page request
     response = requests.get(str(next_page)).text
     soup = BeautifulSoup(response)
#exporting
df = pd.DataFrame(data, columns = ['Book Title', 'Book Stars', 'Book Price', 'Book in Stock?', 'Book URL'])
df.to_csv('ScrappedBooks.csv', sep=';', encoding='utf-8', index=False)