collection = set()

# #1 .add - adds an element
(collection.add(1))
(collection.add(2))
(collection.add(3))
(collection.add((1,1,0)))
(collection.add("True"))
# (collection.add([7,8,9])) #will give error saying "unhashable type"

#2 remove - removs the element
collection.remove()
#3
(collection.clear())

#4 pop
print(collection.pop())
print(collection.pop())
print(collection)

#5 union
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.union(set2))
#6 intersection
print(set1.intersection(set2))





