# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 15:59:53 2019

@author: leona
"""

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