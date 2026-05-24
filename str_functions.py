#ALWAYS ADD A PARENTHESIS IN THE END OFA FUNCTION
#1
a = ("i am a string")
# print(a.endswith("ng")) #will always give boolean value
# print(a.endswith("tion"))

#2
print(a.capitalize())
print(a)

#3
print(a.replace("i","s"))

#4
print(a.find("string")) #will return the index of the first ocurrence of the word
print(a.find("p")) #will always return -1 since -1 is non existent. only existing for slicing ONLY

#5
print(a.count("i"))
