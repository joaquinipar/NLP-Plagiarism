import numpy as np
import sklearn
from sklearn.metrics import jaccard_score
import nltk
from nltk import word_tokenize
from nltk import re
from resources import *
import requests
from bs4 import BeautifulSoup

def scrape(doc1,doc2): # Recibe los nombres de los dos archivos

    if ".doc" in doc1 or ".docx" in doc1:
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
        doc1_data = extract_from_web(doc1)
    else:
        raise TypeError("Document not supported. If you inserted a webpage, make sure that it includes HTTP in the beginning.")

    scraped_data = dict()
    scraped_data[doc1] = doc1_data
    scraped_data[doc2] = doc2_data

    return scraped_data

def score_plagiarism(tok1,tok2): # recibe dos tokens y devuelve un score
    token1 = str2token(tok1)
    token2 = str2token(tok2)
    return jaccard_similarity(tok1,tok2)
    
