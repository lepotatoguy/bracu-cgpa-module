import xlsxwriter
import pandas as pd

course = []
cg = 0

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
    return(list_of_courses)

def get_cgpa():
    weighted_cg = 0
    creds = credits_attempted()
    cg = 0
    for i in range(0,len(course)):
        weighted_cg = weighted_cg + (course[i][1] * course[i][2])
    cg = cg + (weighted_cg / creds)
    return(cg)

def credits_attempted():
    creds = 0
    for i in range(0,len(course)):
        creds = creds + course[i][2]
    return(creds)

def save_to_storage():
    workbook = xlsxwriter.Workbook("CGPA.xlsx")
    outSheet = workbook.add_worksheet()
    
    outSheet.write("A1", "Course")
    outSheet.write("B1", "GPA")
    outSheet.write("C1", "Credits")

    for item in range(0, len(course)):
        outSheet.write(item+1, 0, course[item][0]) #Course
        outSheet.write(item+1, 1, course[item][1]) #GPA
        outSheet.write(item+1, 2, course[item][2]) #Credits
    
    outSheet.write(len(course)+1, 0, "CGPA")
    outSheet.write(len(course)+1, 1, get_cgpa())
    outSheet.write(len(course)+1, 2, "")

    workbook.close()

def read_from_storage(file_path):
    file = pd.read_excel(file_path)
    for item in range(0, len(file.Course)-1):
        add(file['Course'][item], file['GPA'][item], file['Credits'][item])
    test = file['Course'][len(file.Course)-1]
    if "cgpa" not in test.lower():
        cg = get_cgpa()
    else:
        cg = file['GPA'][len(file.Course)-1]

def flush():
    course.clear()
    cg = 0


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

======================================

save_to_storage()
Save to Storage:
This method is to save to PC/Google Colab as a excel file (xlsx).

======================================

======================================

read_from_storage(file_path)
Read from Storage:
This method is to read excel file (xlsx) from PC/Google Colab. 
There is one parameter to pass. file_path (str)
Template File: https://github.com/lepotatoguy/bracu-cgpa-module/blob/main/CGPA.xlsx
Add your course according to your wish like the pattern.
Template Picture: https://i.postimg.cc/1R7q78nt/getfrompc.png

======================================

======================================

flush()
Flush:
This method is to flush all the data of course list and CGPA. 

======================================

I have tried to implement all the functionalities, 
it might have some bugs also. 
Please ignore that or please contact me 
through email to notify me about the bug. 
I will try to give proper credits to that too.

Email: hello@joyantamondal.com
''')
