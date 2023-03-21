# Lab3.1_07_Extra.py
# Extra questions (6,7,8) of lab 3.1. 
# Author: Matthew Arthur

# 6 Why does this expression cause an error? How can you fix it?

# message = 'I have eaten ' + 99 + ' burritos' (commented the commands so that the workaround does not error)
# print(message)

# Error message says  that strings only can be concatenated. As 99 is an integer and not a string, this is causing the program to error. 
# One workaround: 

message = 'I have eaten ' + str(99) + ' burritos'
print(message)


# 7 Why is eggs a valid variable name while 100 is invalid?

# eggs is a valid variable name as it starts with a letter. Variables must start with a letter, not a number. For this reason 100 does not work. numbers can be in the middle or at the end of a variable, just not the first character. 


# 8 What three functions can be used to get the integer, floating-point number, or string version of a value?

# To get the integer value, int() can be used. 
# To get the floating-point number, float() can be used. 
# To get the string version of a number, str() can be used. 
# To figure out what type of value a variable is, type() can be used. 

