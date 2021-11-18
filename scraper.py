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
            price = result.find(class_='result-price').contents
            title = result.find(class_='result-title hdrlnk').contents
            #print(title)
            prices.append(price)
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

connection = sqlite3.connect('craigslist.db')
cursor = connection.cursor()
#cursor.execute('CREATE TABLE listings(listing TEXT, price INT)')
#connection.commit()

#cursor.execute("INSERT INTO listings VALUES('Tiki', 1000)")
#connection.commit()

cursor.execute('SELECT * FROM listings')
data = cursor.fetchall()
sys.stdout = sys.__stdout__
print(data)