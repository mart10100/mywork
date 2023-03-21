# Lab3.2_01_round.py
# This program takes an input float and outputs an integer with the input rounded to the nearest whole number. Help from Lab3.2
# Author: Matthew Arthur


# To try and overcome the issue that the comments in the lab explain (regarding rounding to the nearest number) I have added the additional step in the round function of rounding it to zero decimal places.
# As shown in w3 schools - https://www.w3schools.com/python/ref_func_round.asp#:~:text=The%20round()%20function%20returns,will%20return%20the%20nearest%20integer.
# With this, the rounded number remains as a float. This could be converted to an integer by casting int()
number_to_round = float(input("Enter a float number: "))
rounded_number = round(number_to_round, 0)

# Adding in an extra line (after doing the rounding) to cast rounded_number to an integer:

int(rounded_number)
print('{} rounded is {}'.format(number_to_round,rounded_number))
