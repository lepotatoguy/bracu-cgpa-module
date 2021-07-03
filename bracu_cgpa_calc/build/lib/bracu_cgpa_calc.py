course = []

def add(course_name, course_cgpa, course_credits):
    course.append([course_name, course_cgpa, course_credits])

def remove(course_name):
    courselist = []
    removed = -1
    for i in range(0,len(course)):
        courselist.append(course[i][0])
        
    if course_name in courselist:
        removed = courselist.index(course_name)
        #print(removed)

    if removed == -1:
        return("You have not entered the course / Wrong Course Code.")
    else:
        course.remove(course[removed])
        return(course)

def check_attempted_course():
    list_of_courses = []
    for i in range(0,len(course)):
        list_of_courses.append(course[i][0])
    return list_of_courses

def get_cgpa():
    weighted_cg = 0
    creds = credits_attempted()
    cg = 0
    for i in range(0,len(course)):
        weighted_cg = weighted_cg + (course[i][1] * course[i][2])
    cg = cg + (weighted_cg / creds)
    return cg

def credits_attempted():
    creds = 0
    for i in range(0,len(course)):
        creds = creds + course[i][2]
    return creds

def readme():
    print('''
======================================
Welcome to BracU CGPA Calculator.
This module is created for easy CGPA calculation for BracU Students.
To get started, run bracu_cgpa_calc.docs()
======================================

Created by Joyanta J. Mondal
Email: hello@joyantamondal.com

======================================''')


def docs():
    print('''
======================================

add(course_name, course_cgpa, course_credits)
Add Course(s):
This method is to add course information.
There are three parameters to pass. Course Code (str), Course Grade (int/float), Course Credit Hours (int/float)

======================================

remove(course_name)
Remove Course(s):
This method is to remove course information.
There is one parameter to pass. Course Code (str)

======================================
 
======================================

check_attempted_course()
This method is to check courses attempted which were inputted.
It will return list of courses.

======================================

get_cgpa()
Get CGPA:
This method is to check the CGPA with inputted courses.

======================================

credits_attempted()
Credits Attempted:
This method is to check amount of credits attempted.

======================================

I have tried to implement all the functionalities, 
it might have some bugs also. 
Please ignore that or please contact me 
through email to notify me about the bug. 
I will try to give proper credits to that too.

Email: hello@joyantamondal.com
''')

    

