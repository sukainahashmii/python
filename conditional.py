age = int(input("enter ur age:"))
if(age>=24): #always has a boolean value, and always prints the statement if the condition is TRUE
#if means if the condition is true then statement should be executed
    print("you are old")
    print("you should get married")
    print("you should get successful")
elif(age==23): #elif = else if
    print("do masters")
elif(age==22):
    print("spend time w fam")
#diff btw if and elif is: elif only is applicable when if statement gives false


a = 1
if(a>2):
    print("greater than 2")
elif(a>3):
    print("greater than 3")
#o/p for this will be greater than 2 only. elif statement doesnt get printed bc if statement =became true before itself
else: #if all statements above becomes false, then else statement is executed.
    #else statement can only come once in the code
    print("go home")