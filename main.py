import nltk
from bs4 import BeautifulSoup
import requests
import spacy

webpage_response = requests.get('https://joaquinipar.github.io/blog/Metodologia-de-Sistemas/')
webpage = webpage_response.content

#print(webpage)

webpage_soup = BeautifulSoup(webpage,"html.parser")

#print(webpage_soup.find_all("p"))

strings = []

for p in webpage_soup.find_all("p"):
    strings.append(p.string)

for s in strings:
    print(s)

