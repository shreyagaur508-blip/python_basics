collection = set()
#add elements to the set
collection.add(1)
collection.add(2)
collection.add(3)
print(collection)

#remove an element from the set
collection.remove(2)
print(collection)

#pop an element from the set
collection.pop()    
print(collection)

#union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

#intersection of two sets
print(set1.intersection(set2))

#clear the set
collection.clear()
print(collection)
