# Nlp from scratch
NLP from scratch

## Commands using -

### Importing the spacy package
```
import spacy
```

### Initialized chapter 1
```
1.Introduction_to_spacy
```

## Inside introduction_to_spacy
```
## Example Spacy Usage

In this example, we demonstrate how to use the spaCy library in Python for basic natural language processing tasks.

import spacy

# Initialize the spaCy NLP object for English
nlp = spacy.blank('en')

# Process a text
doc = nlp("Hello World!")

# Print tokens in the processed text
for token in doc:
    print(token.text)

# Access a specific token
token = doc[1]
print(token.text)

# Extract a span of tokens
span = doc[1:3]
print(span.text)

# Process a text with numerical and punctuation tokens
doc = nlp("It costs $5.")

# Print token information
print("Index:  ", [token.i for token in doc])
print("Text:  ", [token.text for token in doc])
print("is_alpha:  ", [token.is_alpha for token in doc])
print("is_punct:  ", [token.is_punct for token in doc])
print("like_num:  ", [token.like_num for token in doc])

```

### Inside_getting_started_file
```
 Blank SpaCy NLP Objects for Multiple Languages

 This repository demonstrates how to create blank spaCy NLP objects for different languages (English, German, and Spanish) and process text using spaCy.

 Installation
 Before running the code, make sure you have spaCy installed. You can install it using pip:

 pip install spacy

Additionally, you'll need to download the language models for the respective languages if you haven't already. You can do this using spaCy's download command:

python -m spacy download en
python -m spacy download de
python -m spacy download es

Part 1: English

In Part 1, we create a blank spaCy NLP object for English using spacy.blank("en"). Then, we process a simple English sentence and print its text.

# Create the English NLP object
nlp = spacy.blank("en")

# Process a text
doc = nlp("This is a sentence.")

# Print the document text
print(doc.text)

Part 2: German

In Part 2, we create a blank spaCy NLP object for German using spacy.blank("de"). Then, we process a German sentence and print its text.

# Create the German NLP object
nlp = spacy.blank("de")

# Process a text
doc = nlp("Liebe Grüße!")

# Print the document text
print(doc.text)

Part 3: Spanish

In Part 3, we create a blank spaCy NLP object for Spanish using spacy.blank("es"). Then, we process a Spanish sentence and print its text.

# Create the Spanish NLP object
nlp = spacy.blank("es")

# Process a text
doc = nlp("¿Cómo estás?")

# Print the document text
print(doc.text)

```