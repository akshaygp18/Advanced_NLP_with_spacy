#What’s not included in a pipeline package that you can load into spaCy?

# 1)A config file describing how to create the pipeline.

# 2)Binary weights to make statistical predictions.

# 3)The labelled data that the pipeline was trained on.

# 4)Strings of the pipeline's vocabulary and their hashes.


#Answer:3)The labelled data that the pipeline was trained on.

#That's correct! Trained pipelines allow you to generalize based on a set of training examples. 
#Once they’re trained, they use binary weights to make predictions. 
#That’s why it’s not necessary to ship them with their training data.