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
import sys
from preprocessing import *



def scrape(doc1,doc2): 

    doc1_data = scrape_doc(doc1)
    doc2_data = scrape_doc(doc2)

    scraped_data = dict()
    scraped_data[doc1] = doc1_data
    scraped_data[doc2] = doc2_data

    return scraped_data


def plagiarism(doc1,doc2=None):

    
    if doc2 is None: # Checks the web
        
        title1 = title(doc1)
        

        print(f"Analizing {title1} and {doc2}")

        best_score = 0
        best_score_title = ""
        for j in search(title(doc1), tld="com.ar",lang='es', num=3, stop=5, pause=2): 
            
            print("Found!")
            print(f"Link: {j}")

            if( is_downloadable(j) ):
                continue
            print(f"Title: {title(j)}")

            if( plagiarism(doc1,j) > best_score ):
                
                best_score = plagiarism(doc1,j)
                print(f"New best score: {best_score}")
                best_score_title = title(j)
        
        print(f"The best score comparison is '{best_score_title}' with a score of {best_score}")
        
        return best_score
    else: # Checks given documents/links
        scraped = scrape(doc1,doc2)
        
        return detect_plagiarism(scraped[doc1],scraped[doc2])
        #return calculate_score(str(scraped[doc1]),str(scraped[doc2]))

def detect_plagiarism(string1,string2):

    doc2 = nlp(string2)
    doc1 = nlp(string1)
    for sent2 in doc2.sents:

        sent2_clean = preprocess(sent2.as_doc().text) # doc type
    
        for sent1 in doc1.sents:
            sent1_clean = preprocess(sent1.as_doc().text) # doc type
            
            sim = sent2_clean.similarity(sent1_clean) 

            if( sim > 0.9 and not is_a_question(sent1.text) and not is_a_question(sent2.text)):
                print("--------------------------------------------------------")
                print(f"Found possible plagiarism between: ")
                print(sent2.text)
                print(f"Paragraph Number: {list(doc2.sents).index(sent2)}")
                print("and")
                print(sent1.text)
                print(f"Paragraph Number: {list(doc1.sents).index(sent1)}")
                print(f"Similarity: {sim}")



documents = list(sys.argv)
if( len(documents) == 1 ):
    print("Error: At least one document/link needs to be provided.")
    sys.exit()

if(len(documents) < 3):
    documents.append(None)

plagiarism(documents[1],documents[2])