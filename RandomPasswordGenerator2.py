# This was my second attempt at making a random password generator.
# Do try it out and please let me know if you find any bugs or issues.

import random
import string
import time

# printable contains letters, digits, punctuation and whitespace (removed by strip()), characters stores it as a string
characters = string.printable.strip()

print("Welcome to this Random Password Generator!")
print("We suggest keeping the length at least 12 characters to ensure that your password is strong.")

try:
    length = int(input("Enter the desired length of the password: "))
except ValueError:
    print("Invalid input. Please enter an integer only.")
    print("By default the length is set to 12.")
    length = 12

print("\nGenerating your random password...\n")
time.sleep(1)
print("Your password is: ")

run = True
while run:
    print("".join(random.choice(characters) for i in range(length)))
    satisfied = input("\nAre you satisfied with this password? yes (y) / no (n): ").lower()
    if satisfied == 'y':
        run = False
    elif satisfied == 'n':
        print("\nYour new password is: ")
        continue
    else:
        print("Invalid input: answer should be in 'y' or 'n'\nWe assume you are satisfied!")
        run = False
