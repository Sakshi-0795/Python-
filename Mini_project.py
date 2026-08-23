#Mini Project:- Number Game
import random

def play_game():
    lucky_num = random.randint(1, 50)

    while True:
        user_num = int(input("Guess the lucky num : "))

        if user_num == lucky_num:
            print("You won. game Over!!!")
            break
        elif user_num < lucky_num:
            print("Too Low")
        else:
            print("To High")
    print("Thank you for playing!!!") 

play_game()