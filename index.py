# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:02:55 2019

@author: leona
"""

#Now from the clean intro and plots we start building the dictionary that will have "index":word, so we have a unique associatioin between a word in the dataset we care about and a number. Obviously we will save it as json file, as many other dictionaries that follow to be able to use them when we want in our search engine.
dictionar = {}
k = 0
for i in range(30000):
    file1 = open("Cleantsv/filmclean-"+str(i)+'.tsv', encoding="utf8") 
    line = file1.read()# Use this to read file content as a stream: 
    #print(line)
    words = line.split('\t') 
    wordssplitted1 = words[14].split()
    wordssplitted2 = words[15].split()
    #print(wordssplitted1, wordssplitted2)
    for i in wordssplitted1:
        #print(type(i))
        if i not in dictionar:
            dictionar[i] = str(k)
            k = k+1
    for i in wordssplitted2:
        #print(type(i))
        if i not in dictionar:
            dictionar[i] = str(k)
            k = k+1
#dictionar
import json

with open('Dictionary.json', 'w') as fp:
    json.dump(dictionar, fp)
#inverted dictionary now
dictionar2 = {}
length = 0
for i in range(30000):
    file = "Cleantsv/filmclean-"+str(i)+'.tsv'
    file1 = open(file, encoding="utf8") 
    line = file1.read()# Use this to read file content as a stream: 
    #print(line)
    words = line.split('\t') 
    wordssplitted1 = words[14].split()
    wordssplitted2 = words[15].split()
    #print(wordssplitted1, wordssplitted2)
    for j in wordssplitted1:
        code = diction[j]
        if code not in dictionar2:
            dictionar2[code] = [file]
        elif file not in dictionar2[code]:
            dictionar2[code].append(file)
    for j in wordssplitted2:
        code = diction[j]
        if code not in dictionar2:
            dictionar2[code] = [file]
        elif file not in dictionar2[code]:
            dictionar2[code].append(file)
#dictionar
import json

with open('Dictionary1.json', 'w') as fp:
    json.dump(dictionar2, fp)
