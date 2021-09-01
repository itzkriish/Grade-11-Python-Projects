# This was the first ever mini-game I created, and so the code is very basic.
# It is a simple, text - based Rock, Paper, Scissors game that is played between the user and the computer.
# Do try it out and please let me know if you find any bugs or issues.

import random
import time

print("Welcome! Lets play Rock Paper Scissors\n")
time.sleep(2)
print("Here are the rules: \n1. Rock beats Scissors \n2. Scissors beats Paper \n3. Paper beats Rock")
print("4. Points: Win = 1 point | Tie = 0  points")
time.sleep(2)
print("\nLets begin!")
time.sleep(2)

user_points = computer_points = 0


# Function to check winner and display score
def score():
    print("\nYour score:", user_points, "\nMy score:", computer_points)
    if user_points > computer_points:
        print("\nCongrats! You beat me!")
    elif user_points == computer_points:
        print("\nIt's a tie! Good game!")
    else:
        print("\nI win! Better luck next time!")


ans = True
options = ['rock', 'paper', 'scissors']
while ans is True:
    computer = random.choice(options)
    user_inp = input("\nChoose: Rock | Paper | Scissors\n").lower()

# Tie
    if computer == user_inp:
        print("You chose", user_inp.upper(), "and computer chose", computer.upper())
        print("It's a tie! \n")

# Rock
    elif user_inp == 'rock':
        if computer == 'paper':
            print("You chose ROCK and computer chose PAPER")
            print("Computer wins \n")
            computer_points += 1
        else:
            print("You chose ROCK and computer chose SCISSORS")
            print("You win \n")
            user_points += 1

# Paper
    elif user_inp == 'paper':
        if computer == 'scissors':
            print("You chose PAPER and computer chose SCISSORS")
            print("Computer wins \n")
            computer_points += 1
        else:
            print("You chose PAPER and computer chose ROCK")
            print("You win \n")
            user_points += 1

# Scissors
    elif user_inp == 'scissors':
        if computer == 'rock':
            print("You chose SCISSORS and computer chose ROCK")
            print("Computer wins \n")
            computer_points += 1
        else:
            print("You chose SCISSORS and computer chose PAPER")
            print("You win \n")
            user_points += 1

# Invalid input
    else:
        print("Please recheck your input \n")

# Play again or quit
    play_again = input("Do you want to continue playing? yes (y) / no (n): ").lower()
    if play_again == 'n':
        score()
        print("Bye! Thanks for playing")
        ans = False
    elif play_again != 'y':
        print("Invalid input: answer should be in 'y' or 'n'")
        print("By default the game continues... \n")
time.sleep(5)
