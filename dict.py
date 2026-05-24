#dictionaries are built in data types in python that stores key value pairs.
# it is used under curly brackets

#there is no order in dicts. no indexes so it is unordered.
#it is mutable, cannot create duplicate keys. repetation for keys, not allowed
info = {
    "key" : "value",
    "name": "naina",
    "hobbies" : ["singing", "music", "cooking", "cleaning" ],
    "topics" : ("string", "lists", "tuples", "dictionaries"),
    "age" : 20, 
    "is_adult": True,
    "marks" : 99.9,
    32.3 : 44.4
}
print(info["name"]) #used to sccess specific value in a dic. through its key
info["name"] = "mirza"
info["surname"] = "baig" #basically does the job of "append functiom"
print(info)

null_dict = {}
null_dict["stud"] = "akshita"
null_dict["age"] = 19

print(null_dict)