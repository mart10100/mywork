# Lab3.3_02_normalise.py
# This program takes an input string and strips any leading or trailing spaces, and converts the string to lower case
# Author: Matthew Arthur (with help from lab 3.3 step 3)

raw_str = input("Please enter a string: ")
normalised_str = raw_str.strip().lower()

raw_str_length = len(raw_str)
normalised_str_length = len(normalised_str)

print(f"That string normailsed is: {normalised_str}")
print(f"We reduced the input string from {raw_str_length} to {normalised_str_length} characters")

# Experimented with using different variable names that were a bit shorter etc, not worth the confusion! 