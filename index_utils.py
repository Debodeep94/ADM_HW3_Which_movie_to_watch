# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:04:48 2019

@author: leona
"""
#I actually didn't define function for this task but if we want to create the dict for like i indexes woukld be like this

def define(ranges):
    dictionar = {}
    k = 0
    for i in ranges:
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

    with open('Diction.json', 'w') as fp:
        json.dump(dictionar, fp)