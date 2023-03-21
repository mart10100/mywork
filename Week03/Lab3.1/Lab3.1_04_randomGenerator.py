# randomGenerator.py
# This program randomly outputs an integer between 1 and 10. 
# Author: Matthew Arthur 

import random

number = random.randint(1,10)

# Modifying to try and allow the user to input the range

print("Here is a random number {}" .format(number))

# Extra - Modifying to try and allow the user to input the range. Thinking to try and base it off the principles used in previous parts of the labs where inputs are assigned variables and then putting them into the program above?
# Limitation of this is that this does not work when the first number in the range is larger than the second number. A workaround for now is that the input instructs the second number for the range is to be larger than the first. 

import random

x = int(input("Enter first number to create a range: "))
y = int(input("Enter second, larger number to create a range: "))

number = random.randint(x,y)

print("Here is a random number between {} and {}: {}".format(x, y, number))
