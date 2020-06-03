import spacy



### Para clasificar tipo de word
#nlp = spacy.load("en_core_web_sm")
#doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

#for token in doc:
#    print(token.text, token.pos_,token.dep_)

### Para similarity

nlp = spacy.load("en_core_web_md")
tokens = nlp("handball football")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text,token2.text,token1.similarity(token2))