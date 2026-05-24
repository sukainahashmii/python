#for loops are used for sequential traversal of different datatypes like list, tuples, string, etc
vegitabli = ["susubumber", "bamberbola", "brinjal"]
for char in vegitabli:
    print(char)

str = "i am from bambrolistan"
for val in str:
    print(val)

tuple = (1, 2, 3, 4, 5)
for int in tuple:
    print(int)

str = "apnacollege"
for char in str:
    if char == 'o':
        print("o found")
        break
    print(char)

print("End")