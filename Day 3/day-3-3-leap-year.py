# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#on every year that is evenly divisible by 4            - Delbart med 4 skottår
#except** every year that is evenly divisible by 100    - Delbart med 100 inte skottår 
#unless** the year is also evenly divisible by 400      - Utom om det är delbart med 100 och 400 (skottår)

#uträkning
four = year % 4
hundred = year % 100
fourhundred = year % 400 

if four == 0:
    if hundred == 0:
        if fourhundred == 0:
            print("Leap year.")
        else: 
            print("Not leap year.")
    else:
        print("Leap year")
else:
    print("Not leap year.")
