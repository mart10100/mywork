# Lab5_01_.py
# This code has been taken from lab 5 and pasted in here to answer the associated questions
# Author: Andrew Beatty

numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [ 12 , 'Fred', False, {}]
someone = dict(firstname = "joe")
me = {
    "firstName" : "Andrew",
    "teaching" : [{
        "courseName" : "programming",
        "semester" : 1
    },{
        "courseName" : "Data Representation",
        "semester" : 2
    }
    ]
}

#   Questions
# a. numberOfQuestions is a variable integer
# b. 'avaerageAge' is a float
# c. debugmode = True' is a boolean
# d. 'name = "joe"' is a string
# e. ages is a list
# f. months is a tuple
# g. months[1] - the first element of the months tuple. 'Jan' is the first element, it is a string
# h. book is an empty dictionary
# i. stuff is a list (containing an int, a str, a bool, and an empty dictionary)
# j. stuff[2] is a string
# k. someone is a dict (written in a different format??)
# l. someone["firstname"] is a string
# m. me is a dictionary
# n. me["teaching"] is a list containing two dictionaries (?)
# o. me["teaching"][0]["semester"] is the first item in teaching ([0]), asking about the semester. This is an integer
# p. me["teaching"][0]["coursename"] is a string (???) Have I been tricked? 

print(type(me["teaching"][0]["semester"]))