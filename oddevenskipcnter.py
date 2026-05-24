#Project 2: The "Odd-Even Skip-Counter" (Focus: for Loops & continue)
#Goal: Loop through a range of numbers from 1 to 20, but use logic to change how they are printed.
for i in range(1,21):
    if i % 5 == 0:
        print(f"......{i} is skipped!")
        continue
        print(i)
    if i % 2 == 0:
          print(f"{i} is even")
    elif i % 2 != 0:
        print(f"{i} is odd")
    
if i == 20:
    print("done")
