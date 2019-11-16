# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:02:01 2019

@author: leona
"""

#the onbly fucntion i used is to clean the documents
import io 
import nltk
import csv
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english')) 
from nltk.stem import PorterStemmer 

 
ps = PorterStemmer() 
#the fuction preprocess the string as asked in the hmk
def preprocess(sentence):
    sentence = sentence.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(sentence)
    filtered_words = [ps.stem(w) for w in tokens if not w in stopwords.words('english')]
    return " ".join(filtered_words)