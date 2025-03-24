# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 07:59:15 2025

@author: omkar
"""

import re

# Searching
x = input("Enter a sentence to search in: ")
search_term = input("Enter the word to search for: ")
if re.search(search_term, x):
    print("Search is successful")
else:
    print("Search is unsuccessful")

# Find all occurrences
x = input("Enter a sentence: ")
find_term = input("Enter the word to find: ")
y = re.findall(find_term, x)
for i in y:
    print(i)

# Iterator starting and ending positions
x = input("Enter a sentence: ")
iter_term = input("Enter the word to find span: ")
for i in re.finditer(iter_term, x):
    y = i.span()
print(y)

# Match with a particular pattern
x = input("Enter a list of words: ")
y = re.findall("[a-z]an", x)
for i in y:
    print(i)

# Match a series of range of characters
x = input("Enter a sentence: ")
y = re.findall("[fcm]an", x)
for i in y:
    print(i)

# Exclude symbols
x = input("Enter a sentence: ")
y = re.findall("[^f-m]an", x)
for i in y:
    print(i)

# Replace string
x = input("Enter a sentence: ")
replace_term = input("Enter the word to replace: ")
new_term = input("Enter the new word: ")
y = re.compile(replace_term)
c = y.sub(new_term, x)
print(c)

# Replace new line with space
x = input("Enter a multiline text (press Enter twice to finish):\n")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
x = "\n".join(lines)
y = re.compile("\n")
c = y.sub(" ", x)
print(c)

# Match digits
x = input("Enter a string with numbers: ")
b = re.findall(r'\d', x)
print(b)

# Count digits
x = input("Enter a string with numbers: ")
b = len(re.findall(r"\d", x))
print(b)

# Match multiple digit patterns
x = input("Enter a series of numbers: ")
y = re.findall(r"\d{4,7}", x)
print(y)

# Count matches of digit patterns
x = input("Enter a series of numbers: ")
y = len(re.findall(r"\d{4,7}", x))
print(y)

# Match 10-digit phone number
x = input("Enter a phone number (format: 123-123-1234): ")
if re.search(r"\d{3}-\d{3}-\d{4}", x):
    print("It is a phone number.")
else:
    print("It is NOT a phone number.")

# Strict phone number format check
x = input("Enter a phone number (strict format: 123-123-1234): ")
if re.search(r"^\d{3}-\d{3}-\d{4}$", x):
    print("It is a valid phone number.")
else:
    print("It is NOT a valid phone number.")

# Match number ending with '55'
x = input("Enter a series of numbers: ")
y = re.search(r"55$", x)
print(y)

# Match number starting with '55'
x = input("Enter a series of numbers: ")
y = re.search(r"^55", x)
print(y)

# Email validation
import re
email = input("Enter an email address: ")
pattern = r"^[a-z]+[a-z0-9._]*@gmail\.com$"
if re.search(pattern, email):
    print("It is a valid Gmail address.")
else:
    print("It is NOT a valid Gmail address.")
