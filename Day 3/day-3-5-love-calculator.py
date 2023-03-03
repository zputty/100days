## 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
sum_true = 0
sum_love = 0

all_name = name1.lower() + name2.lower()

for true in all_name:
    if true == "t":
        sum_true += 1
    if true == "r":
        sum_true += 1
    if true == "u":
        sum_true += 1
    if true == "e":
        sum_true += 1 

for love in all_name:
    if love == "l":
        sum_love += 1
    if love == "o":
        sum_love += 1
    if love == "v":
        sum_love += 1
    if love == "e":
        sum_love += 1   

total = str(sum_true) + str(sum_love)
total = int(total)

if total < 10 or total > 90:
    message = f"Your score is {total}, you go together like coke and mentos."
elif total > 40 and total < 50:
    message = f"Your score is {total}, you are alright together."
else:
   message = f"Your score is {total}."
print(message)