# Lab4.1_02_grade.py
# This program reads input student marks and prints out the corresponding grade. IT also checks that the given grade is valid. 
# Author: Matthew Arthur (with help from lab4.1 step 2)

percentage = int(input("Please enter your percentage: "))

if percentage < 0 or percentage > 100: 
    print(f'{percentage} is an invalid percentage, please enter a number between 0 and 100.')
elif percentage < 40: 
    print('Fail')
elif percentage < 50: 
    print('Pass')
elif percentage < 60: 
    print('Merit1')
elif percentage < 70: 
    print('Merit2')
else:
    print('Distinction')