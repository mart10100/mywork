# Lab3.1_03_div.py
# This program reads two input numbers and divides the first input by the second to give the integer result and remainder. Written using instructiions from Lab3.1. This only works for integers. 
# Author: Matthew Arthur

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer = int(x//y) 
remainder = x%y

print("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))

# I tried changing the integers to floats to see if this would help to allow non-integer values to be used but as in previous videos this did not work foe some numbers such as 1000 / 0.3 which gave the output "1000.0 divided by 0.3 is 3333.0 with remainder 0.100000000000037" 

#x = float(input("Enter first number: "))
#y = float(input("Enter second number: "))
#answer = float(x//y) 
#remainder = x%y

#print("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))

