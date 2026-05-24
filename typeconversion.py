a = 5
b = 6.1
print(a+b) #automatic conversion mean type conversion, here since float val is big, a is converted to float and o/p is float datatype
#c = "5"
#print(a+c) #error occurs because string cant be added w an int, so use typecasting
c = int("5") #typecasting into int
print(type(c))
print(a+c)

d = (str(a))
print("data type of a now is :",type(a))
