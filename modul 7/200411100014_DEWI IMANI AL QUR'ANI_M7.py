def remaiderFunction(data,num): 
    return data % num

slot = remaiderFunction(55,10)
print(slot)

def createHashTable(data):
    return [[None] for i in range(data)]

hashTable = createHashTable(11)
print(hashTable)

def chaining(data,table):
    for i in range(len(data)):
        ind = remaiderFunction(data[i],len(table))
        if table[ind][0] == None:
            table[ind] = [data[i]]
        else:
            table[ind].append(data[i])
        

a = [54,26,93,17,77,31,44,55,20]
chaining(a,hashTable)
print(hashTable)


def searchHash(data,table):
    hashVal = remaiderFunction(data,len(table))
    for i in range(len(table[hashVal])):
        if data == table[hashVal][i]:
            return f"(data berada di slot ke-, {hashVal}, ' indeks ke-', {i})"
           
    return False    


print(searchHash(66,hashTable))
print(searchHash(54,hashTable))
print(searchHash(20,hashTable))
print(searchHash(55,hashTable))
print(searchHash(100,hashTable))