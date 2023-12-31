import spacy

# Load the small English pipeline
nlp = spacy.load("en_core_web_sm")

# Process a text
doc = nlp("she ate the pizza")

# Iterate over the tokens
for token in doc:
    # Print the text and the predicted part-of-speech tag
    print(token.text, token.pos_)


#Predicting Syntactic Dependencies

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)


#Predicting Named Entities

# Process a text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)


#spacy.explain method
#Get quick definitions of the most common tags and labels.

a = spacy.explain("GPE")
print(a)

b = spacy.explain("NNP")
print(b)

c = spacy.explain("dobj")
print(c)