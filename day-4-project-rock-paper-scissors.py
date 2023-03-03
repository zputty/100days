import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
alternative = [rock, paper,scissors]

select = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

select = alternative[select]

#Computer choise
computer = random.randint(0, 2)

#Fan vad lat du är 
draw = f"It is a draw!"
win = f"You win!"
lose = f"You lose!"

print(f"{select}\n Computer chose:\n")
if select == rock:
    if computer == 0:
        print(f"{rock}\n {draw}")
    elif computer == 1:
        print(f"{paper}\n {lose}")
    else:
        print(f"{scissors}\n {win}")
elif select == paper:
    if computer == 0:
        print(f"{rock}\n {win}")
    elif computer == 1:
        print(f"{paper}\n {draw}")
    else:
        print(f"{scissors}\n {lose}")
elif select == scissors:
    if computer == 0:
        print(f"{rock}\n {lose}")
    elif computer == 1:
        print(f"{paper}\n {win}")
    else:
        print(f"{scissors}\n {draw}")
else:
    print("Error try again")