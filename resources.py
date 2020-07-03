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
import spacy
from spacy.lemmatizer import Lemmatizer

nlp = spacy.load("es_core_news_lg")

def process_text(text):
    doc = nlp(text.lower())
    result = []
    for token in doc:
        if token.text in nlp.Defaults.stop_words:
            continue
        if token.is_punct:
            continue
        if token.lemma_ == '-PRON-':
            continue
        result.append(token.lemma_)
    return " ".join(result)

def lemmatize_clean(tokens):
    list1 = [ token.lemma_ for token in tokens]
    return nlp(' '.join(list1))

def preprocess(text):
    return lemmatize_clean( nlp(process_text(text)) )

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
    webpage_response = requests.get(web, allow_redirects=False)
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

def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

dataset_filter_words = ["trabajo","practico","preguntas","tp"]

def title(doc):
    
    if ".doc" in doc:
        return clean_title(doc[:-4].lower())
    elif ".docx" in doc:
        return clean_title(doc[:-5].lower())
    elif ".pdf" in doc:
        return clean_title(doc[:-4].lower())
    elif "http" in doc:
        return clean_title(extract_title_from_web(doc).lower())
    else:
        raise TypeError("Document not supported. If you inserted a webpage, make sure that it includes HTTP in the beginning.")


def clean_title(title):
    new_title = ""
    for word in title:

        if word.isalpha() or word is ' ':
            
            new_title += word

    
    for forbidden_word in dataset_filter_words:

        if forbidden_word in new_title:
            new_title = new_title.replace(forbidden_word,"")
    
    return new_title

#print(title("TP Comercio electronico preguntas.docx"))

def is_a_question(text):

    if '¿' in text and '?' in text:
        return True
    
    if text[0].isnumeric() and text[1] is ')':
        return True
    if text[0] is '¿' and text.endswith('?'):
        return True
    if  text[0] is '¿' and text.endswith('?.'):
        return True
    if text[0].isnumeric() and text[1] is ')':
        return True
