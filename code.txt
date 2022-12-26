# Function to display hashtable
def display_h(hashTable):
    for i in range(len(hashTable)):
       print(i, end = " ")
       
       for j in hashTable[i]:
        print("-->", end = " ")
        print(j, end = " ")
    print()
# Creating Hash table as a nested list.
HashTable = [[] for _ in range(10)]
# Hashing Function to return key for every value.
def Hashing(keyvalue):
   return keyvalue % len(HashTable)
# Insert Function to add values to the hash table
def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)
    
insert(HashTable, 11, 'Artificial_intelligence')
insert(HashTable, 21, 'data_science')
insert(HashTable, 20, 'metaverse')
insert(HashTable, 9, 'automation')
insert(HashTable, 5, 'blockchain')
insert(HashTable, 25,'cloud_computing')
display_h(HashTable)