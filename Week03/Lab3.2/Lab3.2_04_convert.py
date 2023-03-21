# Lab3.2_04_convert.py
# This program takes an input amount of dollars and gives the amount in cents
# Author: Matthew Arthur

# Initial thoughts - Things to do to complete task: convert euro to cent (multiply by 100), take the absolute value of this. Not sure on the order to do these just yet. 

dollar_amount = float(input("Please enter a dollar amount: $"))
abs_cent_amount = abs(dollar_amount * 100)

print("The absolute amount in cent is {}".format(abs_cent_amount))

# Seems to be working ok for any numbers that I have tried. 
# Only issue that I see is that the absolute amount of cent is given with a decimal.
# Ways t ofix this - could convert to and integer (given that thenumber of cents is a whole number) 
# or - us the truncate function? Will try this. Taken from w3 schools - https://www.w3schools.com/python/numpy/numpy_ufunc_rounding_decimals.asp
# Had to try putting the trunc() function in a number of different places. Tried to follow the example on w3 but had problems when trying to import numpy as np. 
# When I tried to run the program with "import numpy as np" at the start and an additional line of "trunc_abs_cent_amount = np.around(abs_cent_amount, 0)"  after line 8 of the code, 
# I got the error "    import numpy as np \nModuleNotFoundError: No module named 'numpy'"

# Not sure how to resolve this at the moment, moving on as its only something small. 