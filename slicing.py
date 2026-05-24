a = ("i love my sister")
str = a[0:7] #i love will be printed. and ending index is not included
print(str)
print(a[10:len(a)]) #last index can be used as the length
print(a[:5]) #a[o:5]
print(a[0:]) #a[0:len(a)]

#-ve indexing
a = ("APPLE")
ch = a[-5:-1]
print(ch)
print(a[-5:])
print(a[:])
