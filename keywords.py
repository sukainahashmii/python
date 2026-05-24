i = 1
while i <= 5:
    print(i)
    if i == 3:
        break #terminates the loop
    i +=1
print("end")


#continue is another keyword in python that functions as skip
i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue #continue ke baad vali cheeze skip hogi
    print(i)
    i += 1

print("end")

i = 1
while i<=10:
    if(i%2!=0):
        i +=1
        continue
    print(i)
    i +=1
