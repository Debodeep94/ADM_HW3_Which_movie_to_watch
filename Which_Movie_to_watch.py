#!/usr/bin/env python
# coding: utf-8

# In[66]:


from __future__ import print_function
import  requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
#import brown
import csv


# In[20]:


movies_url="https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies3.html"

movies_response = requests.get(movies_url)


# In[21]:


soup = BeautifulSoup(movies_response.text, 'html.parser')


# In[22]:


movies_soup = BeautifulSoup(movies_response.text, 'html.parser')


# In[23]:


links=movies_soup.findAll("a")


# In[24]:


movies3=[]
for tag in links:
    page=tag.get('href')
    movies3.append(page)


# In[25]:


len(movies3)


# In[26]:


from urllib.error import URLError,HTTPError,ContentTooShortError
import time


# In[9]:


#j=1
#for i in range(len(movies3)):
    try:
        mv3ur1=requests.get(movies3[i])
        #soup = BeautifulSoup(mv3ur1.content, 'html.parser')
        #soup=soup.prettify("utf-8")
        strg="M3article_"+str(j)+'.html'
        j=j+1
        html_file=open(strg,"w",encoding='utf-8')
        html_file.write(mv3ur1.text)
        html_file.close()
        time.sleep(1)
    except(URLError,HTTPError,ContentTooShortError) as e:
        html=None
        time.sleep(20*60)
    
    


# In[10]:


for i in range(1,len(movies3)): 
    path="C:\\Users\Debodeep\Documents\Sapienza Learning Materials\ADM\ADMHw3\movies3\M3article_"+str(i)+".html"
    with open(path,"r",encoding="utf-8") as f:
      contents=f.read()
      page=BeautifulSoup(contents,'lxml') 


# #### Function for page title

# In[27]:


def title(page):
  return(page.find('h1',class_="firstHeading").get_text('i'))


# #### Function for intro

# In[106]:


def intro(page):
    table=page.find('table',class_="infobox vevent")
    if table != None:
        thres=table.findNextSiblings()
        intr_pg=''
        for i in thres:
            if i.name=="p":
                intr_pg+=i.text
            else: break
        return intr_pg
    elif table!=None:
        content=page.find('div', class_="toc")
        if content!=None:
            thres=content.findPreviousSiblings()
            intr_pg=''
            for i in thres:
                if i.name=="p":
                    intr_pg+=i.text
                else: break
    else: intr_pg="Null"
    return intr_pg


# #### Function for Plot

# In[107]:


def plot(page):
  for i in page.findAll(class_='mw-headline'):
    if i.text=='Plot':
      plt_hd=i.find_parent()
      plt_pg=""
      for i in plt_hd.find_next_siblings():
        if i.name=="p":
          plt_pg+=i.text
        else: break
    else: plt_pg="Null"
    return(plt_pg)


# #### Function for infobox

# In[108]:


def infobox(page):
    
    film_name = 'NA'
    director = "NA"
    producer = "NA"
    writer = "NA"
    starring = "NA"
    music = "NA"
    release_date = "NA"
    runtime = "NA"
    country = "NA"
    language = "NA"
    budget = "NA"
    for i in page.find_all('tr'):
            if page.find('th',{'class': ['summary']})!= None:
                    film_name = page.find('th',{'class': ['summary']} ).text.strip()
            if i.th:
                if(i.th.text.strip() == 'Directed by'):
                    if i.td:
                        director = i.td.text.strip()
                elif(i.th.text.strip() == 'Produced by'):
                    if i.td:
                        producer = i.td.text.strip()
                elif(i.th.text.strip() == 'Written by'):
                    if i.td:
                        writer = i.td.text.strip()
                elif(i.th.text.strip() == 'Starring'):
                    if i.td:
                        starring = i.td.text.strip()
                elif(i.th.text.strip() == 'Music by'):
                    if i.td:
                        music = i.td.text.strip()               
                elif(i.th.text.strip() == 'Release date'):
                    if i.td:
                        release_date = i.td.text.strip()
                elif(i.th.text.strip() == 'Running time'):
                    if i.td:
                        runtime = i.td.text.strip()
                elif(i.th.text.strip() == 'Country'):
                    if i.td:
                        country = i.td.text.strip()
                elif(i.th.text.strip() == 'Language'):
                      language = i.td.text.strip()
                elif(i.th.text.strip() == 'Budget'):
                      budget = i.td.text.strip()
    return(film_name,director,producer,writer,starring,music,release_date,runtime,country,language,budget)


# #### For different tsv files 

# In[63]:


import io
for i in range(1,len(movies3)+1):
    tsvname = 'Mv3tsv_tpi_'+str(i)+'.tsv'
    with io.open(tsvname,"w", encoding="utf-8") as f1: 
            path="C:\\Users\Debodeep\Documents\Sapienza Learning Materials\ADM\ADMHw3\movies3\M3article_"+str(i)+".html"
            with open(path,"r",encoding="utf-8") as f:
                  contents=f.read()
                  page=BeautifulSoup(contents,'lxml') 
                  tsv_writer = csv.writer(f1, delimiter='\t')
            tsv_writer.writerow(['title','intro', 'plot', 'film_name', 'director', 'producer','writer', 'starring', 'music', 'release date', 'runtime', 'country', 'language', 'budget'])
            tsv_writer.writerow([title(page), intro(page),plot(page)]+list(infobox(page)))


# #### A total picture

# In[41]:


import io
import tsv
with open('tsv_M3_total.tsv','w',encoding="utf-8") as f1:
    writer = csv.writer(f1, delimiter='\t')
    header=['title','intro', 'plot', 'film_name', 'director', 
                               'producer','writer', 'starring', 'music', 'release date', 
                               'runtime', 'country', 'language', 'budget']
    writer.writerow(list(header)) 
    for i in range(1,20): 
        path="C:\\Users\Debodeep\Desktop\Movies3\M3article_"+str(i)+".html"
        with open(path,"r",encoding="utf-8") as f:
            contents=f.read()
            page=BeautifulSoup(contents,'lxml')  
          #colns=['title','intro', 'plot', 'film_name', 'director', 
                               #'producer','writer', 'starring', 'music', 'release date', 
                               #'runtime', 'country', 'language', 'budget']
            row= [title(page), intro(page),plot(page)]+list(infobox(page))
          #print(row)
        writer = csv.writer(f1, delimiter='\t')
        writer.writerow(row)
    


# #### Cleansing

# #### Preprocessing text

# In[64]:


import io 
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english')) 
from nltk.stem import PorterStemmer 
ps = PorterStemmer() 
def preprocess(sentence):
    #ps = PorterStemmer()
    sentence = sentence.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(sentence)
    filtered_words = [ps.stem(w) for w in tokens if w not in stopwords.words('english')]
    return " ".join(filtered_words)
for i in range(1,10001):
    file1 = open('C:\Users\Debodeep\Desktop\Movies3\Mv3tsv_tpi_'+str(i)+".tsv", encoding="utf-8") 
    line = file1.read()# Use this to read file content as a stream: 
    #print(line)
    words = line.split('\t') 
    #print(words)
    for j in range(13, len(words)):
        words[j] = preprocess(words[j]).replace('budget','')    
    tsvname = "C:\Users\Debodeep\Documents\Sapienza Learning Materials\ADM\ADMHw3\movies3\Clean_Mv3tsv_tpi_"+str(i)+".tsv"
    with io.open(tsvname, "w", encoding="utf-8") as out_file:
        #with open(tsvname, 'w') as out_file:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            tsv_writer.writerow(['title','intro', 'plot', 'film_name', 'director', 'producer','writer', 'starring', 'music', 'release date', 'runtime', 'country', 'language', 'budget'])
            tsv_writer.writerow(words[13:])


# In[66]:


words[20]


# #### Creating dictionary

# In[31]:


mv3_dictionary = {}
k = 0
for i in range(1,10001):
    file1 = open("Clean_Mv3tsv_tpi_"+str(i)+'.tsv', encoding="utf8") 
    line = file1.read()# Use this to read file content as a stream: 
    #print(line)
    words = line.split('\t') 
    wordssplitted1 = words[14].split()
    wordssplitted2 = words[15].split()
    #print(wordssplitted1, wordssplitted2)
    for i in wordssplitted1:
        #print(type(i))
        if i not in mv3_dictionary:
            mv3_dictionary[i] = str(k)
            k = k+1
    for i in wordssplitted2:
        #print(type(i))
        if i not in mv3_dictionary:
            mv3_dictionary[i] = str(k)
            k = k+1
#dictionary
import json

with open('Dictionary_Mv3.json', 'w') as fp:
    json.dump(mv3_dictionary, fp)


# In[210]:


import pandas as pd
import json
with open(r"Dictionary_Mv3.json", 'r') as file:
    data = file.read()
dictionary_3 = json.loads(data)
dictionary_3.keys()


# #### creating inverted index

# In[379]:


dictionar3 = {}
length = 0
for i in range(1,10000):
    file = "Clean_Mv3tsv_tpi_"+str(i)+'.tsv'
    file1 = open(file, encoding="utf8") 
    line = file1.read()# Use this to read file content as a stream: 
    #print(line)
    words = line.split('\t') 
    wordssplitted1 = words[14].split()
    wordssplitted2 = words[15].split()
    docs=wordssplitted1+wordssplitted2
    #print(wordssplitted1, wordssplitted2)
    for j in wordssplitted1:
        code = dictionary_3[j]
        if code not in dictionar3:
            dictionar3[code] = [file]
        elif file not in dictionar3[code]:
            dictionar3[code].append(file)
    for j in wordssplitted2:
        code = dictionary_3[j]
        if code not in dictionar3:
            dictionar3[code] = [file]
        elif file not in dictionar3[code]:
            dictionar3[code].append(file)
            
        
#dictionar
import json

with open('Dictionary3.json', 'w') as fp:
    json.dump(dictionar3, fp)


# In[380]:


import pandas as pd
import json
with open(r"Dictionary3.json", 'r') as file:
    data = file.read()
dic3 = json.loads(data)


# ### Search Engine

# In[36]:


import numpy
y = list(input().split())
def searchengine1(y):
    for i in range(len(y)):
        y[i]= preprocess(str(y[i]))
    #Now I tranform the list of input in a list of the codes in the dictiionary based on the input
    yfinal=[] #use this because some words have no match in the vocabulary
    for i in range(len(y)):
        #print(y[i])
        if y[i] in dictionary_3:
            yfinal.append(dictionary_3[y[i]])
    #Now I have to search inside the lists of values from the keys i found and see if some films match in the various keys.
    if  len(yfinal)<len(y):
        return print('We are sorry there are no films, in my database, that match All the words you gave me !(')
    else:
        #print(yfinal)
        starting_values = dic3[yfinal[0]]
#print(starting_values)
        final_values = starting_values.copy()
        for codes in range(1,len(yfinal)):
        #print(codes)
            for film in final_values:
            #print(film)
                if film not in dic3[yfinal[codes]]:
                    final_values.remove(film)
        megaDataframe = pd.DataFrame(columns = ['Title', 'Intro', 'Url'])
    #megaDataframe
        if not final_values:
            return print("Wow no film matched my quiery, I need more films to compare!")
        else:
            k=0
            for document in final_values:
                totakeurl = document.replace("Clean_Mv3tsv_tpi_",'')
                totakeurl = int(totakeurl.replace('.tsv', ''))
                url = movies3[totakeurl]
                temporary = pd.read_csv("C:\\Users\Debodeep\Desktop\Movies3\Mv3tsv_tpi_"+str(totakeurl)+".tsv",delimiter="\t" )
                title = temporary['title'][0]
                intro =  temporary['intro'][0].replace('\r\n','')
                new_row = [title, intro, url]
                megaDataframe.loc[k]=new_row
                k=k+1
            return (megaDataframe)
searchengine1(y)


# ## TF-IDF

# In[377]:


import math
#def function(k):
for i in range(1,10000):# will add more files
    file = "Clean_Mv3tsv_tpi_"+str(i)+'.tsv'
    file1 = open(file, encoding="utf8") 
    line = file1.read() 
    words = line.split('\t') 
    wordssplitted1 = words[14].split()
    wordssplitted2 = words[15].split()
    L=wordssplitted1+wordssplitted2
    for k in dictionary_3:
        tf=L.count(k)/len(L)
#Number of documents containing the kth word is the length of the list obtained from the inverted index.
        idf=math.log(10000/float(len(dic3[dictionary_3[k]])))
        tfidf=tf*idf
        print(tfidf)


# In[376]:




