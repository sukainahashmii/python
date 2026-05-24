#1 append
list = [1,2,3]
list.append(56)

#2 sort. reverse sort
# list.sort(reverse = True) #adds a new element to the end of the list
print(list)
list.sort()
print(list)

#w alphabets
list2 = ['a', 'f', 'e', 'x', 'q', 'k', 'm', 's', 'r']
list2.sort()
print(list2)
list2.sort(reverse = True)
print(list2)

#3 insert
list2.insert(0,"apple") #(index(where), what u want to insert)
print(list2)

#4. remove
list2.remove('apple')
print(list2)

#5. pop
list2.pop(4)
print(list2)

