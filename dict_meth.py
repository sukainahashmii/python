stud ={
    "name" : "akshita",
    "age" : 19,
    "marks" : {
        "eng" : 10, 
        "math" : 15,
        "comp" : 20
    },
    "bauni" : True,
    "bestie" : True
}

#1 returns all keys
print(stud.keys())
print(len(list(stud.keys()))) #dhamakkka, function ke andar function


# #2 returns the no of key:value pairs
print(len(stud))

#3 returns all values
print(list(stud.values()))

# #4.item - returns all key:value pairs
print(list(stud.items())) #if i dont typecast it into a list and try accesing using indexes,it shows error.
pair = list(stud.items())#this is bc dictionaries are unorganised having no index. so it is necessary to typecast it into a list before accessing anything specifically
print(pair[0])

#5 .get - returnsvalue when key is typed
print(stud["name"]) #will give error when key is written galat
print(stud.get("name")) #will not give error -> None instead if in case of mistake
#print(stud["name2"]) 
print(stud.get("name2"))

#6 update - add new key value pairs
(stud.update({"badguy" : "hamza"}))
print(stud)
