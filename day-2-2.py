# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#formel: bmi=weight/hight^2

#Gör om inputs (som är strängar) till floats i stoppar in dem i respektive variabel
bmi_height = float(height)
bmi_weight = float(weight)

#Gör uträkningen enligt formeln | ** = ^
bmi = (bmi_weight / bmi_height ** 2)

#Gör om floats till int och printar reslutatet av uträkningen
print(int(bmi))

# 100 days:
#bmi = int(weight) / float(height) ** 2
#bmi_as_int = int(bmi)
#print(bmi_as_int)
