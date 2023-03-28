# Lab5_02_months.py
# This program uses a tuple to stor ethe months of the year. 
# Author: MAtthew Arthur

months = (
"January", 
"February", 
"March", 
"April",
"May", 
"June", 
"July", 
"August", 
"September", 
"October", 
"November", 
"December"
)

summer_months = months[4:7] # Accidentally did [4:6] but this did not include the 6th list item. 
print(summer_months)

# How it is done in the lab: 
summer = months[4:7]
for month in summer:
    print(month)

# This works better because it prints in the format that is asked in the lab. 