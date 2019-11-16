# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 15:57:17 2019

@author: leona
"""

from bs4 import BeautifulSoup
import requests
import json
soup = BeautifulSoup(open('C:/Users/leona/Desktop/ADMHMK-3/movies2.html'), "html.parser")
soup.head()
lst_a = soup.select('a')
urls = []
for i in lst_a:
    urls.append(i.get('href'))
urls[0]
soup = BeautifulSoup(open('C:/Users/leona/Desktop/ADMHMK-3/movies1.html'), "html.parser")
soup.head()
lst_a = soup.select('a')
lst_a
for i in lst_a:
    urls.append(i.get('href'))
urls[10000]   
soup = BeautifulSoup(open('C:/Users/leona/Desktop/ADMHMK-3/movies3.html'), "html.parser")
soup.head()
lst_a = soup.select('a')
lst_a
for i in lst_a:
    urls.append(i.get('href'))
urls[20000] 
dicturls = {}
for i in range(len(urls)):
    dicturls[i] = urls[i]
with open('dicturls.json', 'w') as fp:
    json.dump(dicturls, fp)
with open(r"C:\Users\leona\Desktop\ADMHMK-3\dicturls.json", 'r') as file:
    data = file.read()
dicturls = json.loads(data) 
from urllib.error import URLError, HTTPError, ContentTooShortError
import time
def getwikipageshtml(urls):
    k=0
    for i in range(len(urls)):
        try:
            ur_l = requests.get(urls[i])
            soup = BeautifulSoup(ur_l.content, 'html.parser')
            soup = soup.prettify("utf-8")   
            stringa = 'Articles/article-'+str(k)+'.html'
            k = k+1
            Html_file= open(stringa, "wb")
            Html_file.write(soup)
            Html_file.close()
        except(URLError,HTTPError, ContentTooShortError)  as e:
            html = None
        #time.sleep(0.001) #Actually for this task we don't need to stop anytime
    return
getwikipageshtml(urls)
