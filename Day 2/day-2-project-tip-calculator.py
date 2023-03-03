#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n"))
tip = float(input("What percentage tip would you like to give? 10, 12, 15?\n"))
split = float(input("How many people to split the bill?\n"))

total = (tip / 100 * bill + bill) / split
#Round the number to decimals
total_and_round = round(total, 2)
#Formatted so the last decimal will show, even if it's a zero
total_and_round = "{:.2f}".format(total_and_round)
message = f"Each person should pay: {total_and_round}"

print(message)