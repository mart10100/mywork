# Lab3.1_06_randomfruit2.py
# This program prints out a random fruit (from a given tuple). Written using lab3.1
# Author: Matthew Arthur

import random

fruits = ('Apple', 'Pear', 'Banana', 'Orange')

# To get a random fruit between 0 and length-1 (?): 
index = random.randint(0,len(fruits)-1)

fruit = fruits[index] 
print("A random fruit is: {}".format(fruit))
