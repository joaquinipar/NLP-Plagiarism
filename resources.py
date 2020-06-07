import numpy as np
import sklearn
from sklearn.metrics import jaccard_score
import nltk
from nltk import word_tokenize
from nltk import re
import docx2txt
from tika import parser
import requests
from bs4 import BeautifulSoup

def scrape_doc(doc):
    if ".docx" in doc: 
        return extract_from_doc(doc)
    elif ".pdf" in doc:
        return extract_from_pdf(doc)
    elif "http" in doc:
        return extract_from_web(doc)
    else:
        raise TypeError("Document not supported. If you inserted a webpage, be sure that it includes HTTP in the beginning.")


def str2token(string_data):
    tokens = word_tokenize(string_data)
    lowercased_tokens = list(map(lambda x: x.lower(),tokens))
    word_tokenized = [word for word in lowercased_tokens if re.search("\w",word)]
    return word_tokenized

def jaccard_similarity(query, document):
    intersection = set(query).intersection(set(document))
    print(intersection)
    union = set(query).union(set(document))
    print(union)
    return len(intersection)/len(union)

def extract_from_doc(name_file):
    text = docx2txt.process(name_file)
    return text

def extract_from_pdf(name_file):
    raw = parser.from_file(name_file)
    return(raw['content'])

def extract_from_web(web):
    webpage_response = requests.get(web)
    webpage = webpage_response.content
    webpage_soup = BeautifulSoup(webpage,"html.parser")
    doc1_data = []
    for p in webpage_soup.select("p"):
        if not (p.getText() is None):
            doc1_data.append(p.getText())
    return list(filter(lambda x: not (x is None) ,doc1_data))
    
def extract_title_from_web(web):
    webpage_response = requests.get(web)
    webpage = webpage_response.content
    webpage_soup = BeautifulSoup(webpage,"html.parser")
    if webpage_soup.find("title") is None: # If there's not a title, returns link
        return web
    return webpage_soup.find("title").string

def title(doc):
    
    if ".doc" in doc:
        return doc[:-4]
    elif ".docx" in doc:
        return doc[:-5]
    elif ".pdf" in doc:
        return doc[:-4]
    elif "http" in doc:
        return extract_title_from_web(doc)
    else:
        raise TypeError("Document not supported. If you inserted a webpage, make sure that it includes HTTP in the beginning.")


