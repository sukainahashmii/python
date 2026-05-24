#Goal: Create a script that locks the user out unless they type the correct master secret key, but gives them exactly 3 attempts.
master_key = "potty123" #secret key
cnt = 0
while cnt < 3:
    user = input("enter secret key:")
    if master_key == user:
        print("correct!")
        print("system unlocked!")
        break
    else:
        cnt += 1
        print(f"wrong pw!{3-cnt} attempts left ")
if cnt == 3:
    print("system locked!")

    
    

        
