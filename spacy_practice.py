import spacy


nlp = spacy.load("en_core_web_md")
tokens = nlp("i was walking between two big dogs")
tokens2 = nlp("there was a person walking in the middle of two giant dogs")
tokens3 = nlp("No use complaining, no point in singing the blues")
tokens4 = nlp("But the president was unclear about the speed and full scope of the actions, and his remarks left many questions unanswered. Stock markets rose after Mr. Trump’s speech in the White House Rose Garden, suggesting that investors had feared the president would take even more draconian steps against China, the world’s second-largest economy.")
tokens5 = nlp("I'm feeling the pressure I can't break out No one can hear me scream and shout Get out of my face, out of my mind I see your corruption I'm not blind I'll carry the burden and take the strain And when I am done I will make you pay")

print(tokens4.text,tokens5.text,tokens4.similarity(tokens5))

