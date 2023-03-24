# Lab4.1_01_is_even.py
# This program takes an input number and tells if it's even or odd
# Author: Matthew Arthur (with help from lab 4.1 step 1)

number = int(input("Enter an integer: "))

if (number % 2) == 0: 
    print(f'{number} is an even number')
else: 
    print(f'{number} is an odd number')