import numpy as np
import sklearn
from sklearn.metrics import jaccard_score
import nltk
from nltk import word_tokenize
from nltk import re
from resources import *



str1 = "The man was walking on the street."
str2 = "The man was walking around the street"

str = "i was walking between two big dogs"
str3 = "there was a person walking in the middle of two giant dogs"
str4 = "No use complaining, no point in singing the blues"
str5 = "But the president was unclear about the speed and full scope of the actions, and his remarks left many questions unanswered. Stock markets rose after Mr. Trump’s speech in the White House Rose Garden, suggesting that investors had feared the president would take even more draconian steps against China, the world’s second-largest economy."
str6 = "I'm feeling the pressure I can't break out No one can hear me scream and shout Get out of my face, out of my mind I see your corruption I'm not blind I'll carry the burden and take the strain And when I am done I will make you pay"

def plagiarism(doc1,doc2): # Recibe los nombres de los dos archivos

    if ".doc" in doc1 or ".docx" in doc1:
        print("doc1 is a doc/x")
        doc1_data = extract_from_doc(doc1)
        print(doc1_data)
    if ".pdf" in doc1:
        print("doc1 is a pdf")
        doc1_data = extract_from_pdf(doc1)
        print(doc1_data)
    if ".doc" in doc2 or ".docx" in doc2:
        print("doc2 es doc/x")
        doc2_data = extract_from_doc(doc2)
        print(doc2_data)
    if ".pdf" in doc2:
        print("doc2 es pdf")
        doc2_data = extract_from_pdf(doc2)
        print(doc2_data)
    

 
plagiarism("MKT 2016 - Alan Szpigiel - TP4 (2).pdf","Trabajo Práctico 1 - Hernan Dalle Nogare.docx")



#extract_from_pdf("MKT 2016 - Alan Szpigiel - TP4 (2).pdf")
#extract_from_doc("Trabajo Práctico 1 - Hernan Dalle Nogare.docx")

def score_plagiarism(tok1,tok2): # recibe dos tokens y devuelve un score
    token1 = str2token(tok1)
    token2 = str2token(tok2)
    return jaccard_similarity(tok1,tok2)
    

#print(score_plagiarism(str1,str2))
