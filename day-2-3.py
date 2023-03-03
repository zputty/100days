# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#todo: Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# 365 days = 1 year
# 52 weeks = 1 year
# 12 months = 1 year

#Total time
#total_life_days = 90 * 365 # 32850 days in total life span
#total_life_weeks = 90 * 52 # 4680 weeks in a total life span
#total_life_months = 90 * 12 # 1080 months in a total life span

#Current time
#lived_days = int(age) * 365 #total lived days
#lived_weeks = int(age) * 52 # total lived weeks
#lived_months = int(age) * 12 # total lived months

#Time left
#days_left = total_life_days - lived_days
#weeks_left = total_life_weeks - lived_weeks
#months_left = total_life_months - lived_months

#To see time left valus
#print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

#100 days:
age_as_int = int(age)

years_remaning = 90 - age_as_int
days_remaning = years_remaning * 365
weeks_remaning = years_remaning * 52
months_remaning = years_remaning * 12
message = f"You have {days_remaning} days, {weeks_remaning} weeks and {months_remaning}"
print(message)