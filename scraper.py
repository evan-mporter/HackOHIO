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
    # print(yahoo.text[0:500]) #Shows the first 500 words of the html of the site

    #reads the html and makes sense of the structure
    s = BeautifulSoup(craigslist.text, 'html.parser') 
    #finds all the span sections with the class attribute equal to what is listed
    results = s.findAll('li', class_='result-row') 
    sys.stdout = open('test.html', 'w')
    print(len(results)) #prints how many span sections found that fit the description
    #price = result.text
    return results

def printList(results):

    for result in results:
        print(result)

results = getPrice(website)
printList(results)
