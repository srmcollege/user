

import nltk

nltk.download('punkt')
from nltk.tokenize import sent_tokenize


user_input = input("Enter a sentence: ")

c = sent_tokenize(user_input)
print(c)


import nltk

nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Take user input
user_input = input("Enter a sentence: ")

# Tokenize the input into words
tokens = word_tokenize(user_input)
print(tokens)

