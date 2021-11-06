import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import operator
from functools import reduce


website = 'https://www.facebook.com/marketplace/category/vehicles'

def getPrice(website):
    facebook = requests.get(website)
    # print(yahoo.text[0:500]) #Shows the first 500 words of the html of the site

    #reads the html and makes sense of the structure
    s = BeautifulSoup(facebook.text, 'html.parser') 
    #finds all the span sections with the class attribute equal to what is listed
    result = s.find('span', attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}) 
    #print(len(result)) #prints how many span sections found that fit the description
    price = result.text
    return price
