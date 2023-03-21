# Lab3.2_03_floor.py
# This prgram takes an input float and outputs an integer rounded down. 
# Author: Matthew Arthur (with help from lab 3.2 step 3)

import math # I do not understand this yet (having only started week 3)

num_to_floor = float(input("Enter a float number: "))
floored_num = math.floor(num_to_floor)
print('{} floored is {}'.format(num_to_floor, floored_num))