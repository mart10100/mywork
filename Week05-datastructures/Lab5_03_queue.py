# Lab5_03_queue.py
# This program puts 10 random numbers into a queue and outputs each number in order, followed by the remaining numbers (?) 
# Author: MAtthew Arthur 

# First thoughts: Need to first make a random queue. Could use somrthing like that random thing from a few weeks ago. - import random

# Will probably need to use a while loop or something, reminds me of the countdown to take off example from last week. 

import random

queue = []
number_of_numbers = 10
range_to = 100

#for numbers in queue: 
#    print(number_of_numbers)

for n in range (0, number_of_numbers): 
      queue.append(random.randint(0,range_to)) # This is the bit that really got me confused. I stioll don't get the "for n in range... part" Could have looked it up but it was right there!

print (f'Queue is {queue}')

while len(queue) != 0: 

    current_number = queue.pop(0)
    print (f'Current number is {current_number} and the queue is {queue}.')

print ('The queue is now empty.')


# I had no idea how to do this. Had to look at the answer. All I was able to do as import random (from week 4 lab), add veriable of number of numbers. 
