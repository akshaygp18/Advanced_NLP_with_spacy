## Part-1: English

## Use spacy.blank to create a blank English("en") nlp object.
## Create a doc and print its text.

#import spacy
import spacy

# Create the english nlp object
nlp = spacy.blank("en")

# Process a text
doc = nlp("This is a sentence.")

# Print the document text
print(doc.text)


## Part-2: German

## Use spacy.blank to create a blank German("de") nlp object.
## Create a doc and print its text.

#import spacy
import spacy

# Create the english nlp object
nlp = spacy.blank("de")

# Process a text
doc = nlp("Liebe Grüße!")

# Print the document text
print(doc.text)


## Part-3: Spanish

## Use spacy.blank to create a blank Spanish("es") nlp object.
## Create a doc and print its text.

#import spacy
import spacy

# Create the english nlp object
nlp = spacy.blank("es")

# Process a text
doc = nlp("¿Cómo estás?")

# Print the document text
print(doc.text)