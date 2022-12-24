hashTable = [[], ] * 10


def checkifPrime(n):
    if n == 1 or n == 0:
      return 0
    for i in range(2, n//2):
      if n % i == 0:
        return 0
    return 1


def getPrime(n):
    if n % 2 == 0:
       n = n + 1
    while not checkifPrime(n):
       n += 2
    return n


def hashFunc(key):
    capacity = getPrime(10)
    return key % capacity


def insertData(key, data):
    index = hashFunc(key)
    hashTable[index] = [key, data]


def removeData(key):
    index = hashFunc(key)
    hashTable[index] = 0


#insertData(123, "Qunatum_computing")
#insertData(456, "Edge_computing")
#insertData(789, "Blockchain")
#insertData(312, "Cyber_security")
#print(hashTable)
#removeData(123)
#print(hashTable)
