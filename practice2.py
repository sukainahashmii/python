for el in range(1,101):
    print(el)

for val in range(100,0,-1):
    print(val)

n = 2
seq = range(11)
for val in seq:
    print(n*val)

1
n = int(input("enter no:"))
sum = 0
i = 1
while i<=n:
    sum += i
    i += 1

print("the sum is", sum)

2
i = 1
factorial = 1
n = 5
for el in range(1,n+1):
    factorial *= i
    i+=1
print(factorial)

#3
i = 1
factorial = 1
n = 5
while i<=5:
    factorial *= i
    i+=1
print(factorial)
    


n = int(input("enter no:"))
if((n*1==n) and ()):  
    print("prime number")
else:
    print("not prime")
n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")