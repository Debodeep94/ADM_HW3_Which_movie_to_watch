# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:09:18 2019

@author: leona
"""

import json
with open(r"C:\Users\leona\Desktop\ADMHMK-3\dicturls.json", 'r') as file:
    data = file.read()
dicturls = json.loads(data) 
import pandas as pd
with open(r"C:\Users\leona\Desktop\ADMHMK-3\Dictionary.json", 'r') as file:
    data = file.read()
diction = json.loads(data)
with open(r"C:\Users\leona\Desktop\ADMHMK-3\Dictionary1.json", 'r') as file:
    data = file.read()
diction2 = json.loads(data)
with open(r"C:\Users\leona\Desktop\ADMHMK-3\ncontain.json", 'r') as file:
    data = file.read()
ncontain = json.loads(data) #dict with number of times a word appear in all the cod
with open(r"C:\Users\leona\Desktop\ADMHMK-3\idfdict.json", 'r') as file:
    data = file.read()
idfdict = json.loads(data) #dict with the idf for every word
with open(r"C:\Users\leona\Desktop\ADMHMK-3\Dictionary2.json", 'r') as file:
    data = file.read()
diction3 = json.loads(data)
 #second inverted dictionary wit doc and tfidf for eevry word
with open(r"C:\Users\leona\Desktop\ADMHMK-3\dicturls.json", 'r') as file:
    data = file.read()
dicturls = json.loads(data) 
with open(r"C:\Users\leona\Desktop\ADMHMK-3\Dicti3.json", 'r') as file:
    data = file.read()
dicti3 = json.loads(data) #first dict with every word and a unique value
with open(r"C:\Users\leona\Desktop\ADMHMK-3\Dictitrue3.json", 'r') as file:
    data = file.read()
dicti_true3 = json.loads(data) #first dict with every word and a unique value

import math
import io 
import nltk
import csv
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english')) 
from nltk.stem import PorterStemmer 
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
from scipy.spatial.distance import cosine

def simple_dot(a, b):
    dsum = 0.
    for ((idx,), val) in np.ndenumerate(a):
        dsum += float(val) * float(b[idx])
    return dsum

def l2_norm(a):
    return math.sqrt(np.dot(a, a))

def cosine_similarity(a, b):
    return np.dot(a,b) / (l2_norm(a)* l2_norm(b))

 
ps = PorterStemmer() 
#the fuction preprocess the string as asked in the hmk
def preprocess(sentence):
    sentence = sentence.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(sentence)
    filtered_words = [ps.stem(w) for w in tokens if not w in stopwords.words('english')]
    return " ".join(filtered_words)
#HERE i DEFINE THE FUCTION TO RECEIVE THE DATASET, GIVEN AN INPUT
#y = list(input('Hello I am engine1, if you give me a string I will do my best to get you a file!').split())
def searchengine1(y):
    if not y:
        return print("You should must give me the string, errrrrrrror")
    for i in range(len(y)):
        y[i]= preprocess(str(y[i]))
    #Now I tranform the list of input in a list of the codes in the dictiionary based on the input
    yfinal=[] #use this because some words have no match in the vocabulary
    for i in range(len(y)):
        #print(y[i])
        if y[i] in diction:
            yfinal.append(diction[y[i]])
    #Now I have to search inside the lists of values from the keys i foundb and see if some films match in the various keys.
    if  len(yfinal)<len(y):
        return print('We are sorry there are no films, in my database, that match ALL the words you gave me !(')
    else:
        starting_values = diction2[yfinal[0]]
        final_values = starting_values.copy()
        for codes in range(1,len(yfinal)):
            new = []
            #print(final_values)
            for film in final_values:                
                if film in diction2[yfinal[codes]]:
                    new.append(film)
            final_values = new
            #print(final_values)
        megaDataframe = pd.DataFrame(columns = ['Title', 'Intro', 'Url'])
        if not final_values:
            return print("Wow no film matched my quiery, I need more films to compare!")
        else:           
            k=0
            for document in final_values:
                totakeurl = document.replace('Cleantsv/filmclean-','')
                totakeurl = str(int(totakeurl.replace('.tsv', '')))
                url = dicturls[totakeurl]
                temporary = pd.read_csv('C:/Users/leona/Desktop/ADMHMK-3/Tsvfiles/'+'film'+(totakeurl)+'.tsv', delimiter='\t' )
                title = temporary['title'][0]
                intro =  temporary['intro'][0].replace('\r\n','')
                new_row = [title, intro, url]
                megaDataframe.loc[k]=new_row
                k=k+1
            return print(megaDataframe)
#A = searchengine1(y)




#HERE i DEFINE THE FUCTION TO RECEIVE THE DATASET, GIVEN AN INPUT
import heapq as hq
def tf(word, doc):
    return doc.count(word) / len(doc)
#y = list(input('Hello I am engine2 and if you give me a string I will give you a better list of films than my brother engine1!').split())
def searchengine2(y):
    if not y:
        return print("You should must give me the string, errrrrrrror")
    for i in range(len(y)):
        y[i]= preprocess(str(y[i]))
    #Now I tranform the list of input in a list of the codes in the dictiionary based on the input
    yfinal=[] #use this because some words have no match in the vocabulary
    for i in range(len(y)):
        #print(y[i])
        if y[i] in diction:
            yfinal.append(diction[y[i]])
    #Now I have to search inside the lists of values from the keys i foundb and see if some films match in the various keys.
    if  len(yfinal)<len(y):
        return print('We are sorry there are no films, in my database, that match ALL the words you gave me !(')
    else:
        starting_values = diction2[yfinal[0]]
        final_values = starting_values.copy()
        for codes in range(1,len(yfinal)):
            new = []
            for film in final_values:
                if film in diction2[yfinal[codes]]:
                    new.append(film)
            final_values = new
        megaDataframe = pd.DataFrame(columns = ['Title', 'Intro', 'Url', 'Similarity'])
        if not final_values:
            return print("Wow no film matched my quiery, I need more films to compare!")
        else:  
            lstofl = []
            #here there is a lstofl that has vectors associated with every document, in order of final_values
            for film in final_values:
                item = []
                for code in yfinal:
                    for value in diction3[code]:
                        if film in value:
                            item.append(value[1])
                            break
                lstofl.append(item) 
            #print(lstofl)
            #Now I have to create the inquiry vector and get the cosine similarity of beetween it and every component of lstofl 
            query = []
            for i in y:
                query.append(tf(i,y)*idfdict[i])
            cossim = []
            for vector in lstofl:
                cossim.append(cosine_similarity(query, vector))
            #print(cossim) #the cosine similariotyb in order of apparition of my document
            dict_sim = {}
            for indx in range(len(cossim)):
                sim = cossim[indx]
                if sim not in dict_sim:
                    dict_sim[sim]=[final_values[indx]]
                else:
                    dict_sim[sim].append(final_values[indx])
            #print(dict_sim)
            Peak = 20
            #HERE THE HEAP ALGORITHM
            cossim = list(set(cossim))
            to_select = hq.nlargest(Peak, cossim)   
            k=0
            #print(to_select)
            #Now i have the name key(cossim) and values(docum) and I have to take the first 15 of them.
            for i in to_select:
                if(k<Peak):
                    for document in dict_sim[i]:
                            if(k>Peak):
                                return print(megaDataframe)
                            totakeurl = document.replace('Cleantsv/filmclean-','')
                            totakeurl = str(int(totakeurl.replace('.tsv', '')))
                            url = dicturls[totakeurl]
                            Similarity = format(i, '.10g')
                            temporary = pd.read_csv('C:/Users/leona/Desktop/ADMHMK-3/Tsvfiles/'+'film'+(totakeurl)+'.tsv',delimiter='\t' )
                            title = temporary['title'][0]
                            intro =  temporary['intro'][0].replace('\r\n','')
                            new_row = [title, intro, url, Similarity]
                            megaDataframe.loc[k]=new_row
                            k=k+1
            return  print(megaDataframe)


import json

def splitTextToDouble(string):
    words = string.split()
    grouped_words = [' '.join(words[i: i + 2]) for i in range(0, len(words), 2)]
    return grouped_words
from textblob import TextBlob as tb


def n_containing(word, doclist):
    return sum(1 for doc in doclist if word in doc.split())

def score_function(doc, lizt, z, x, d):
    average = 266
    score = 0
    half = 0
    diri = 0
    da = pd.read_csv('C:/Users/leona/Desktop/ADMHMK-3/'+doc, delimiter = '\t')
    intro_plot = da['plot'][0]+da['intro'][0]
    for i in list(set(lizt)):
        score = score + tf(i, intro_plot)
    ln = len(lizt)
    for i in range(ln):
        #print(da)
        if lizt[i] in da['title'][0].split() and x == 'n':
            score = score + 1
        if ln>1 and i < ln-1:
            if x =='ye' and lizt[i]+' '+lizt[i+1] in splitTextToDouble(da['starring'][0]):
                half = half + 25
            if d == 'ye' and lizt[i]+' '+lizt[i+1] in splitTextToDouble(da['director'][0]):
                diri = diri + 20
        elif ln<=1:
            if lizt[i] in da['starring'][0].split():
                half = half + 5
            if lizt[i] in da['director'][0].split():
                diri = diri + 5
        lizt = list(set(lizt))
        for i in lizt:
            if i in da['starring'][0]:
                score = score + 3
            if i in da['director'][0]:
                score = score + 6
    #print(half)
    if z == da['language'][0]:
        score = score + 4
    #print(x)
    if x == 'ye':
        score = score + half
    value = len(intro_plot.split())
    if value >= average+90:
        score = score + 4
    if value < (average):
        score = score -4
    na = 0
    for i in da.values[0]:
        if i == 'na':
            na = na +1
    if na > 3:
        score = score - 4
    #print(score)
    return score



#y = list(input('Welcome in search engine3, write a string and, after some more questions I will give you a very likely film you can be looking for!\n').split())
#z = input('Write your preferred language: \n')
#x = input('You gave an actor/actress name in the string? type ye or n \n')
#d = input('You gave also a director name in the string?type ye or n \n')
def searchengine3(y, z, x, d):
    if not y:
        return print("You should must give me the string, errrrrrrror")
    for i in range(len(y)):
        y[i]= preprocess(str(y[i]))
    #Now I tranform the list of input in a list of the codes in the dictiionary based on the input
    yfinal=[] #use this because some words have no match in the vocabulary
    for i in range(len(y)):
        #print(y[i])
        if y[i] in dicti3:
            yfinal.append(dicti3[y[i]])
    #Now I have to search inside the lists of values from the keys i foundb and see if some films match in the various keys.
    if  len(yfinal)<len(y):
        return print('We are sorry there are no films, in my database, that match ALL the words you gave me !(')
    else:
        starting_values = dicti_true3[yfinal[0]]
        final_values = starting_values.copy()
        for codes in range(1,len(yfinal)):
            new = []
            for film in final_values:
                if film in dicti_true3[yfinal[codes]]:
                    new.append(film)
            final_values = new
        megaDataframe = pd.DataFrame(columns = ['Title', 'Intro', 'Url', 'Score'])
        #print(final_values)
        if not final_values:
            return print("Wow no film matched my quiery, I need more films to compare!")
        else:  
            dict_score = {}
            score_list = []
            Threshold  = 8
            k_limit = 5
            #print(final_values)
            for doc in final_values:
                #score_function is the function I create and used to give points to every film
                x = preprocess(x)
                z = preprocess(z)
                d = preprocess(d)
                score = score_function(doc, y, z, x, d)
               # print(score)
                if score not in dict_score:
                    dict_score[score]=[doc]
                    score_list.append(score)
                else:
                    dict_score[score].append(doc)
            score_list = list(set(score_list))
            #print(dict_score)
            best = hq.nlargest(Threshold, score_list)
            k = 0
            #print(best)
            for score in best:
                #print(score)
                if k < k_limit :
                    for document in dict_score[score]:
                        #print(document)
                        if k < k_limit:
                            totakeurl = document.replace('Cleantsv/filmclean-','')
                            totakeurl = str(int(totakeurl.replace('.tsv', '')))
                            url = dicturls[totakeurl]
                            Score = score
                            temporary = pd.read_csv('C:/Users/leona/Desktop/ADMHMK-3/Tsvfiles/'+'film'+(totakeurl)+'.tsv',delimiter='\t' )
                            title = temporary['title'][0]
                            intro =  temporary['intro'][0].replace('\r\n','')
                            new_row = [title, intro, url, Score]
                            megaDataframe.loc[k]=new_row 
                            #print(megaDataframe)
                            k = k+1
                        else:
                            return print(megaDataframe)
                else:
                    return print(megaDataframe)
            return print(megaDataframe)
query = int(input('We have 3 engines, please write the number 1, 2 or 3 for the engine you would like to use for your query.\nWrite here: '))
if query == 1:
    y = list(input('Hello I am engine1, if you give me a string I will do my best to get you a file!\nInsert string: ').split())
    searchengine1(y)
elif query == 2:
    y = list(input('Hello I am engine2 and if you give me a string I will give you a better list of films than my brother engine1!\nInsert string: ').split())
    searchengine2(y)
elif query == 3:
    y = list(input('Welcome in search engine3, write a string and, after some more questions I will give you a very likely film you can be looking for!\nInsert string ').split())
    z = input('Write your preferred language: \n')
    x = input('You gave an actor/actress name in the string? type ye or n : \n')
    d = input('You gave also a director name in the string?type ye or n : \n')
    searchengine3(y,z,x,d)
else:
    print('Hey hey hey you didn\'t give me a number between 1, 2 or 3')
