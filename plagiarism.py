import numpy as np
import sklearn
from sklearn.metrics import jaccard_score
import nltk
from nltk import word_tokenize
from nltk import re
from resources import *
import requests
from bs4 import BeautifulSoup
from googlesearch import search

def scrape(doc1,doc2): 

    if ".docx" in doc1: 
        doc1_data = extract_from_doc(doc1)
    elif ".pdf" in doc1:
        doc1_data = extract_from_pdf(doc1)
    elif "http" in doc1:
        doc1_data = extract_from_web(doc1)
    else:
        raise TypeError("Document not supported. If you inserted a webpage, be sure that it includes HTTP in the beginning.")

    if ".doc" in doc2 or ".docx" in doc2:
        doc2_data = extract_from_doc(doc2)
    elif ".pdf" in doc2:
        doc2_data = extract_from_pdf(doc2)
    elif "http" in doc2:
        doc2_data = extract_from_web(doc2)
    else:
        raise TypeError("Document not supported. If you inserted a webpage, make sure that it includes HTTP in the beginning.")

    scraped_data = dict()
    scraped_data[doc1] = doc1_data
    scraped_data[doc2] = doc2_data

    return scraped_data


def plagiarism(doc1,doc2=None):

    print(f"Analizing {doc1} and {doc2}")

    if doc2 is None: # Checks the web
        
        best_score = 0
        best_score_title = ""
        for j in search(title(doc1), tld="com", num=3, stop=3, pause=2): 
            
            print(j)
            print(title(j))

            if( plagiarism(doc1,j) > best_score ):
                
                best_score = plagiarism(doc1,j)
                print(best_score)
                best_score_title = title(j)
        
        print(f"The best score comparison is {best_score_title} with a score of {best_score}")
        return best_score
    else: # Checks given documents/links
        scraped = scrape(doc1,doc2)
        return calculate_score(str(scraped[doc1]),str(scraped[doc2]))

def calculate_score(str1,str2): 
    return nltk.jaccard_distance(set(str1),set(str2))


