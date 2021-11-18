from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import operator
from functools import reduce
import sys
import sqlite3

city = input("Enter a city name: ")

website = 'https://' + str(city) + '.craigslist.org/d/cars-trucks/search/cta'
print(website)
prices = []
titles = []

#connects to database and creates table if it doesn't already exist
connection = sqlite3.connect('craigslist.db')
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS listings")
cursor.execute("CREATE TABLE listings (listing TEXT, price REAL);")


def getPrice(website):
    craigslist = requests.get(website)
    s = BeautifulSoup(craigslist.text, 'html.parser') 
    numOfListings = s.find('span', attrs={'class':'totalcount'})
    count = int(numOfListings.text)
    print(count)
    page = 0
    results = []
    sys.stdout = open('wayne.html', 'w')
    #finds all the span sections with the class attribute equal to what is listed
    while count > 0:
        craigslist = requests.get(website)
        #results.append(s.findAll('li', class_='result-row'))
        listings = s.findAll('li', class_='result-row')

        for result in listings:
            #gets the listing names and prices
            price = result.find(class_='result-price').contents
            title = result.find(class_='result-title hdrlnk').contents
            #makes the prices into floats
            price[0] = price[0].replace('$', '').replace(',', '') 
            fixed_price = float(price[0])
            #inserts listing names and prices into sql database
            cursor.execute("INSERT INTO listings VALUES (?, ?);", (title[0], fixed_price))
            connection.commit()
            prices.append(fixed_price)
            titles.append(titles)
            try: 

                print(title, 'PRICE: ', price)
            except UnicodeEncodeError:
                print('ERROR: Cannot Encode Character(s) in Title')

            

        count -= 120
        page += 120
        website = 'https://' + str(city) + '.craigslist.org/d/cars-trucks/search/cta?s=' + str(page) 
    return results

#def createMap():
    #index = 0
    #map = dict({})
    #for title in titles:
        #map[title] = prices[index]
        #index += 1
    #return map
        


results = getPrice(website)
#map = createMap()

#for i in range(len(results)):
    #print(titles[i])
    #print(prices[i])