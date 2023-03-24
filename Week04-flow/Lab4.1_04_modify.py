# Lab4.1_04_modify.py
# This program prompts for a number to be input until -1 is input. 
# Author: Matthew Arthur (with help from lab 4.2)

end_number = -1

number = int(input("Please enter an integer: "))

while number != end_number: 
    print("Please enter a different number")
    number = int(input("Another number: "))

print("-1 is the number that ends this loop.")
