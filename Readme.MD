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