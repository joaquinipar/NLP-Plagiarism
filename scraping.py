#import requests

#webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')
#print(webpage_response.text)
#webpage = webpage_response.content
#print(webpage) ## String con toda la estructura html del sitio

import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://joaquinipar.github.io/blog/Metodologia-de-Sistemas/')
webpage = webpage_response.content

#print(webpage)

webpage_soup = BeautifulSoup(webpage,"html.parser")

#print(webpage_soup.find_all("p"))

strings = []

for p in webpage_soup.select('p'):
    
    if not (p.getText() is None):
        strings.append(p.getText())
        #print(p.string)
        #print("APPEND!----------------------------------------------------------------------------------------------")

for s in strings:
    print(s)