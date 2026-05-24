#tuples are also IMMUTABLE like strings. only LIST is mutable
tup = (2, 3, 4, 5)
print(type(tup))
# accessing specific elements
print(tup[0])
tup1 = (1,)#right way of writing a tuple
print(tup1)
print(type(tup1))

#slicing
print(tup[:3])