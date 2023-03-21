# Lab3.1_05_randomfruit.py
# This program prints out the name of a random fruit. 
# Author: Matthew Arthur

import random

fruits = ['Apple', 'Pear', 'Banana', 'Orange']

# To get a random fruit between 0 and length-1 (?): 
index = random.randint(0,len(fruits)-1)

fruit = fruits[index] 
print("A random fruit is: {}".format(fruit))