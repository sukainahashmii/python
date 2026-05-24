a = int(input("enter ur marks:"))
if(a>=90):
    print("grade A")
elif(90>a>=80):
    print("grade B")
# elif(80>a>70):
#     print("grade C")
# else:
#     print("grade D")

marks = int(input("enter ur marks:"))
if(marks >= 90):
    grade = "A"
elif(marks<90 and marks>=80):
    grade = "B"
elif(marks>=70 and marks<80):
    grade = "C"
else:
    grade = "D"
print("ur grade is:", grade)

#nesting (if statement ke andar if statement)
age = int(input("enter ur age:"))
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive!")
else:
    print("too young, dont drive")