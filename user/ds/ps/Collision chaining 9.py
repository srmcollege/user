# Function to display hashtable
def display_hash(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()
  
# Creating Hashtable as 
# a nested list.
HashTable = [[] for _ in range(10)]
  
# Hashing Function to return 
# key for every value.
def Hashing(keyvalue):
    return keyvalue % len(HashTable)
  
  
# Insert Function to add
# values to the hash table
def insert(HashTable, keyvalue, value):
      
    hash_key = Hashing(keyvalue)
    HashTable[hash_key].append(value)
  
# Driver Code
insert(HashTable, 10, 'Allahabad')
insert(HashTable, 22, 'Mumbai')
insert(HashTable, 20, 'Mathura')
insert(HashTable, 9, 'Delhi')
insert(HashTable, 21, 'Punjab')
insert(HashTable, 21, 'Noida')
insert(HashTable, 23, 'maharshtra')
insert(HashTable, 24, 'gujrat')
insert(HashTable, 11, 'abc')
insert(HashTable, 43, 'pune')
insert(HashTable, 64, 'xyz')  
display_hash(HashTable)
