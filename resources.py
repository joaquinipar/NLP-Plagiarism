import numpy as np
import sklearn
from sklearn.metrics import jaccard_score
import nltk
from nltk import word_tokenize
from nltk import re
import docx2txt
from tika import parser

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