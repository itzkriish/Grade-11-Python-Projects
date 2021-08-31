# This was my first attempt of making a random password generator.

# Project: Random password generator
# NOTE: I am just a beginner at python and have just started.
# I know there will be more effective ways to do this but with my knowledge this is what I could do

import random
import time

num = list(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
abc = list(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
            'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'])
ABC = list(['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
            'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'])
sym = list(['-', '_', '@', '^', '#', '*', '(', ')'])

a = random.choice(num)
b = random.choice(abc)
c = random.choice(ABC)
d = random.choice(sym)
e = random.choice(ABC)
f = random.choice(abc)
g = random.choice(num)
h = random.choice(sym)

print("Welcome to this random password generator")
print("The password generated is 8 characters long")
print("Generating your random password...")

time.sleep(1)

print("Your password is: ")
lst = list()
options = [a, b, c, d, e, f, g, h]
for i in range(len(options)):
    char = random.choice(options)
    lst.append(char)
    options.remove(char)
x = ''.join(lst)
print(x)
