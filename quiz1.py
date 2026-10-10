import random

choices = ["rock","paper","scissors"]

user = input("Enter rock, paper or scissors").lower()
computer = random.choice(choices)

print("Computer:", computer)

if user == computer:
    print("Draw!")
elif(user == "rock" and computer == "scissors")or  (user == "paper"and computer == "rock") or (user == "scissors" and compuuter == "paper"):
    print("You Win!!! Congratulations")
else:
    print("Computer wins!!!")



