# sub.py
# This program subtracts a first number input from a second number input. This has been completed with direction from lab3.1. As stated in the lab this converts a string into an integer, allowing the mathematic operation to be completed. A limitation of this program is that non-integer values cannot be computed. 
# Author: Matthew Arthur 

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer = x-y
print("{} minus {} is {}".format(x, y, answer))

