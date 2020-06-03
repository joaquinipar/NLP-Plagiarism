import numpy as np
import sklearn
from sklearn.metrics import jaccard_score
import nltk
from nltk import word_tokenize
from nltk import re

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

str1 = "The man was walking on the street."
str2 = "The man was walking around the street"

str = "i was walking between two big dogs"
str3 = "there was a person walking in the middle of two giant dogs"
str4 = "No use complaining, no point in singing the blues"
str5 = "But the president was unclear about the speed and full scope of the actions, and his remarks left many questions unanswered. Stock markets rose after Mr. Trump’s speech in the White House Rose Garden, suggesting that investors had feared the president would take even more draconian steps against China, the world’s second-largest economy."
str6 = "I'm feeling the pressure I can't break out No one can hear me scream and shout Get out of my face, out of my mind I see your corruption I'm not blind I'll carry the burden and take the strain And when I am done I will make you pay"


print(str2token(str))
print(str2token(str3))

print( jaccard_similarity(str1, str2) )
