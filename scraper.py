import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import operator
from functools import reduce
import sys

city = input("Enter a city name: ")

website = 'https://' + str(city) + '.craigslist.org/d/cars-trucks/search/cta'
print(website)

def getPrice(website):
    craigslist = requests.get(website)
    s = BeautifulSoup(craigslist.text, 'html.parser') 
    numOfListings = s.find('span', attrs={'class':'totalcount'})
    count = int(numOfListings.text)
    print(count)
    page = 0
    results = set()
    #finds all the span sections with the class attribute equal to what is listed
    while count > 0:
        craigslist = requests.get(website)
        results = results.append(s.findAll('li', class_='result-row')) 
        sys.stdout = open('wayne.html', 'w')
        print(len(results)) 
        count -= 120
        page += 120
        print(count)
        website = 'https://' + str(city) + '.craigslist.org/d/cars-trucks/search/cta?s=' + str(page) 
    return results

def printList(results):

    for result in results:
        print(result)

results = getPrice(website)
printList(results)
