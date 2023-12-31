#The pipelines we’re using in this course are already pre-installed. 
#For more details on spaCy’s trained pipelines and how to install them on your machine, see the documentation.

# Use spacy.load to load the small English pipeline "en_core_web_sm".
# Process the text and print the document text.

import spacy

# Load the "en_core_web_sm" pipeline
nlp = spacy.load("en_core_web_sm")


text = "It's official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Process the text
doc = nlp(text)

# Print the document text
print(doc.text)