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

## Inside_getting_started_file
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

## Inside documents_spans_tokens_file
```
Processing Text and Selecting Tokens with spaCy

This repository demonstrates how to use spaCy, a popular natural language processing library, to process text and select specific tokens from a document. The code is divided into two parts:

Part 1: Selecting the First Token

In this part, we create an English spaCy NLP object using spacy.blank("en"). Then, we process a text and create a Doc object. Finally, we select and print the text of the first token in the document.

# Import spaCy and create the English NLP object
import spacy

nlp = spacy.blank("en")

# Process the text
doc = nlp("I like tree kangaroos and narwhals.")

# Select the first token
first_token = doc[0]

# Print the first token's text
print(first_token.text)

Part 2: Selecting Token Slices

In this part, we again create an English spaCy NLP object using spacy.blank("en"), process a text, and create a Doc object. We demonstrate how to select slices of tokens from the document.

We create a slice of the Doc for the tokens "tree kangaroos" and print its text.
We create a slice of the Doc for the tokens "tree kangaroos and narwhals" (excluding the period) and print its text.

# Import spaCy and create the English NLP object
import spacy

nlp = spacy.blank("en")

# Process the text
doc = nlp("I like tree kangaroos and narwhals.")

# A slice of the Doc for "tree kangaroos"
tree_kangaroos = doc[2:4]
print(tree_kangaroos.text)

# A slice of the Doc for "tree kangaroos and narwhals" (without the ".")
tree_kangaroos_and_narwhals = doc[2:6]
print(tree_kangaroos_and_narwhals.text)
```

## Inside lexical_attributes_file
```
Finding Percentages in Text Using spaCy

This code demonstrates how to use spaCy to find percentages in a text by iterating through tokens in a document. Specifically, it looks for two subsequent tokens: a number and a percent sign ("%").

Steps:

Initialize spaCy:
We start by initializing a blank spaCy NLP object for the English language (en).

import spacy

nlp = spacy.blank("en")

Process the Text:
Next, we process the input text using the spaCy NLP object, creating a Doc object.

doc = nlp("In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are.")

Iterate Over Tokens:
We then iterate over each token in the Doc object to analyze its content.

for token in doc:

Check for Numbers:
For each token, we check if it resembles a number using the like_num token attribute.

if token.like_num:

Check for the Next Token:
If a token resembles a number, we get the next token in the document by accessing the doc[token.i + 1] position.

next_token = doc[token.i + 1]

Check for the Percent Sign:
Finally, we check if the next token's text attribute is equal to the percent sign "%". If it is, we print the percentage found.

if next_token.text == "%":
    print("Percentage found:", token.text)

This code is useful for extracting percentages from text data where percentages are represented as numbers followed by a percent symbol. It leverages spaCy's token attributes and object-oriented structure to efficiently process and extract this information from text.
```

## Inside Trained_pipelines_file
```
# NLP with spaCy

This Python code showcases spaCy for natural language processing tasks:

- **Part-of-Speech Tagging**: Identifying parts of speech in text.
- **Syntactic Dependency Prediction**: Predicting word dependencies.
- **Named Entity Recognition**: Extracting named entities.
- **spacy.explain Method**: Getting tag and label explanations.

See code examples in the respective sections below.

```

## Inside Pipeline_package_file
```
# What's not included in a spaCy Pipeline Package

This README provides an explanation of what is not included in a pipeline package that you can load into spaCy, along with the correct answer.

## Question

What’s not included in a pipeline package that you can load into spaCy?

1) A config file describing how to create the pipeline.

2) Binary weights to make statistical predictions.

3) The labeled data that the pipeline was trained on.

4) Strings of the pipeline's vocabulary and their hashes.

## Answer

The correct answer is:

**3) The labeled data that the pipeline was trained on.**

Explanation: Trained pipelines allow you to generalize based on a set of training examples. Once they’re trained, they use binary weights to make predictions. That’s why it’s not necessary to ship them with their training data.
```

## Inside Loading_pipeline_file
```

1. Import the spaCy library at the beginning of your Python script:

import spacy

Load the "en_core_web_sm" pipeline using spacy.load():
nlp = spacy.load("en_core_web_sm")

This step loads the small English pipeline for natural language processing.
Define the text you want to process:
text = "It's official: Apple is the first U.S. public company to reach a $1 trillion market value"
Replace this text with your own if needed.

Process the text using the loaded pipeline:
doc = nlp(text)
This step tokenizes and analyzes the input text, creating a doc object.

Access and print the document text:
print(doc.text)
This will display the processed document text.
```

## Inside Predicting_linguistic_annotation_file
```

Part 1:
Import the spaCy library and load the "en_core_web_sm" model, which is a small English language model.

Define a sample text.

Process the text using the loaded spaCy model, creating a doc object.

Iterate over each token in the doc and print:

token_text: The text of the token.
token_pos: The part-of-speech (POS) tag of the token.
token_dep: The dependency label of the token.
This loop provides information about the grammatical properties of each word in the text.

Part 2:
Import spaCy and load the "en_core_web_sm" model (if not already loaded).

Define a different sample text.

Process the text using spaCy, creating a doc object.

Iterate over the entities recognized in the text (entities are typically named entities like names, dates, organizations, etc.) using doc.ents.

Print each entity's:

ent.text: The text of the entity.
ent.label_: The label or category of the entity (e.g., ORGANIZATION, DATE, etc.).
This loop extracts and prints named entities and their corresponding labels from the text.
```