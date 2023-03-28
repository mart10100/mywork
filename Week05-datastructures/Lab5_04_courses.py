# Lab5_04_courses.py
# This program stores a student name and list of here courses, and gives her course mark. 
# Author: Matthew Arthur

# First thoughts: Obviously use a dictionary as that's what it is asking. Need to get a better understanding of dictionarires in general. 
# 

student = {
    "name" : "Mary",
    "modules" : [ 
        {
                "course_name" : "Programming",
                "grade" : 67
        }, 
        {
            "course_name" : "History",
            "grade" : 56
        },
    
    ]
}

print (f' student: {student["name"]}')
for module in student ["modules"]: 
    print (f'\t{module["course_name"]}: \t{module["grade"]}')   #Took somw fiddling but was able to use the more up to date formatting. 
