# Lab4.1_03_grade2.py
# This program reads input (can be int or not) student marks and prints out the corresponding grade. It also checks that the given grade is valid. 
# Author: Matthew Arthur (with help from lab4.1)

# This is from step 3 of the lab. Two ways to modify this to round x9.5 up: 
# 1. Set the percentages < x9.5 instead of the whole number
# 2. Use the round function on the inital input. 


# 1. This requires changing the percentage input to a float (may cause some issues for numbers that can't be written in binary)

percentage = float(input("Please enter your percentage: "))

if percentage < 0 or percentage > 100: 
    print(f'{percentage} is an invalid percentage, please enter a number between 0 and 100.')
elif percentage < 39.5: 
    print('Fail')
elif percentage < 49.5: 
    print('Pass')
elif percentage < 59.5: 
    print('Merit1')
elif percentage < 69.5: 
    print('Merit2')
else:
    print('Distinction')



# 2. Round the initial input (https://www.w3schools.com/python/ref_func_round.asp#:~:text=The%20round()%20function%20returns,will%20return%20the%20nearest%20integer.)

percentage = round(float(input("Please enter your percentage: ")))

if percentage < 0 or percentage > 100: 
    print(f'{percentage} is an invalid percentage, please enter a number between 0 and 100.')
elif percentage < 39.5: 
    print('Fail')
elif percentage < 49.5: 
    print('Pass')
elif percentage < 59.5: 
    print('Merit1')
elif percentage < 69.5: 
    print('Merit2')
else:
    print('Distinction')