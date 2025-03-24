# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 19:00:19 2025

@author: ASUS
"""
####################


import nltk

nltk.download('punkt_tab')

word="Shreyas"
c=nltk.sent_tokenize(word)
print(c)

####################


import nltk

nltk.download('punkt')

sentence="Shreyas"
c=nltk.sent_tokenize(sentence)
print(c)

####################


import nltk

nltk.download('punkt')

with open(r"E:\Jim1.txt","r")as file:
    word=nltk.word_tokenize(file.read())
print(word)

####################
