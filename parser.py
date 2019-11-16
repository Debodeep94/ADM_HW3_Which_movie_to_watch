# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:00:24 2019

@author: leona
"""

import csv
import io
for i in range(30000):
    filename = "Articles/article-"+str(i)+".html"
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        soup = BeautifulSoup(data, 'html.parser')
        #Now That I opened the file I have to look for the section asked
        #first I take the title and clear him of spaces and the word -Wikipedia
        titlepage = soup.title.string
        titleonly = titlepage.split("- Wikipedia")
        titlepage = titleonly[0].strip()
        #now I create empty string as intro and plot
        intro = ''
        plot = ''
        #Now i searcvh the first paragraph that usually or is empty or is the intro
        start = soup.find('p')
        intro = start
        intro1 = start.text
        B = ''
        #in B I put m,y limit for the paragraphs in the intro, because after this h2 there will always be the plot
        B = intro.find_next_sibling('h2')
        if(B!=None and B.find_next_sibling('p')):
            C = B.find_next_sibling('p')
            while(C != intro.find_next_sibling('p')): 
                intro1 = intro1 + intro.find_next_sibling('p').text
                intro = intro.find_next_sibling('p')
            plot = ''    
            #then i do the same with the plot, so I start at B and end in the next h2
            plot = B
            plot1 = ''
            compare = ''
            if(B.find_next_sibling('h2')):
                compare = B.find_next_sibling('h2')
                compareto = compare.find_next_sibling('p')
                while(compareto != plot.find_next_sibling('p')):
                    plot1 = plot1 + plot.find_next_sibling('p').text
                    #print(plot1)
                    plot = plot.find_next_sibling('p')
                    #if plot or intro are empty I put NA
        if(intro1 == ''):
            intro1 = "NA"
        if plot1 == '':
            plot1 = "NA"
        #Now I start working on the other features
        intro = intro1
        plot = plot1
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
#'film_name', 'director', 'producer','writer', 'starring', 'music', 'release date', 'runtime', 'country', 'language', 'budget'
        for link in soup.find_all('tr'):
            if soup.find('th',{'class': ['summary']})!= None:
                    film_name = soup.find('th',{'class': ['summary']} ).text.strip()
            if link.th:
#I just check in the th and if I find the class I need I take the relative td. Some of them are inaccessible so the if link.td
                if(link.th.text.strip() == 'Directed by'):
                     director = link.td.text.strip()
                elif(link.th.text.strip() == 'Produced by'):
                      producer = link.td.text.strip()
                elif(link.th.text.strip() == 'Written by'):
                    writer = link.td.text.strip()
                elif(link.th.text.strip() == 'Starring'):
                    starring = link.td.text.strip()
                elif(link.th.text.strip() == 'Music by'):
                     music = link.td.text.strip()               
                elif(link.th.text.strip() == 'Release date'):
                    if link.td:
                        release_date = link.td.text.strip()
                elif(link.th.text.strip() == 'Running time'):
                    runtime = link.td.text.strip()
                elif(link.th.text.strip() == 'Country'):
                    if link.td:
                        country = link.td.text.strip()
                elif(link.th.text.strip() == 'Language'):
                    if link.td:
                        language = link.td.text.strip()
                elif(link.th.text.strip() == 'Budget'):
                    budget = link.td.text.strip()
#now I open the tsv files and create one for every film.        
        tsvname = 'Tsvfiles/'+'film'+str(i)+'.tsv'
        with io.open(tsvname, "w", encoding="utf-8") as out_file:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            tsv_writer.writerow(['title','intro', 'plot', 'film_name', 'director', 'producer','writer', 'starring', 'music', 'release date', 'runtime', 'country', 'language', 'budget'])
            tsv_writer.writerow([titlepage, intro, plot, film_name, director, producer, writer, starring, music, release_date, runtime, 
                 country, language, budget])
Now we clean The files, so we first define a preprocess function to do it!

import io 
import nltk
import csv
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english')) 
from nltk.stem import PorterStemmer 
​
 
ps = PorterStemmer() 
#the fuction preprocess the string as asked in the hmk
def preprocess(sentence):
    sentence = sentence.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(sentence)
    filtered_words = [ps.stem(w) for w in tokens if not w in stopwords.words('english')]
    return " ".join(filtered_words)
for i in range(30000):
    file1 = open('Tsvfiles/film'+str(i)+'.tsv', encoding="utf8") 
    line = file1.read()# Use this to read file content as a stream: 
    words = line.split('\t') 
    for j in range(13, len(words)):
        words[j] = preprocess(words[j])
        if j ==13:
            #Here for the format of tsv files and my split('\t') the word budget would always be in my title, so I take her out
            words[j] = words[j].replace('budget ','')  
            words[j] = words[j].replace('budget\n\n','')
        print(words[j])
    tsvname = "Cleantsv/filmclean-"+str(i)+'.tsv'
    with io.open(tsvname, "w", encoding="utf-8") as out_file:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            tsv_writer.writerow(['title','intro', 'plot', 'film_name', 'director', 'producer','writer', 'starring', 'music', 'release date', 'runtime', 'country', 'language', 'budget'])
            tsv_writer.writerow(words[13:])
