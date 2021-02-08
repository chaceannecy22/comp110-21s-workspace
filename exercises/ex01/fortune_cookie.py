"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730421780"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("You're fortune cookie says...")

fortune: int = randint(1,4)

if fortune == 1:
    print["You will encounter an event that will positively change your life forever!"]
else:

    if fortune == 2:
        print["Trust your gut in the next battle you face and your dreams will come true!"]
    else:

        if fortune == 3:
            print["True love is just around the corner! Keep your head up."]
        else:
            print["Life will suprise you. Try doing the unexpected and see what happens..."]

