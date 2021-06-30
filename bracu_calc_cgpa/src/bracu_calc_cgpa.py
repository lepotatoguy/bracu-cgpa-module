course = []

def add(course_name, course_cgpa, course_credits):
    course.append([course_name, course_cgpa, course_credits])

def remove(course_name):
    removed = -1
    for i in range(0,len(course)):
        if course_name in course[i][0]:
            removed = course[i].index(course_name)

    if removed == -1:
        return("You have not entered the course / Wrong Course Code.")
    else:
        course.remove(course[removed])
        return(course)

def check_attempted_course():
    for i in range(0,len(course)):
        return(course[i][0])

def get_cgpa():
    weighted_cg = 0
    creds = credits_completed()
    cg = 0
    for i in range(0,len(course)):
        weighted_cg = weighted_cg + (course[i][1] * course[i][2])
    cg = cg + (weighted_cg / creds)
    return cg

def credits_completed():
    creds = 0
    for i in range(0,len(course)):
        creds = creds + course[i][2]
    return creds

def readme():
    print("======================================")
    print("Welcome to BracU CGPA Calculator.")
    print("This module is created for easy CGPA calculation for BracU Students.")
    print("To get started, run cgpa_calc_bracu.docs()")
    print("======================================")
    print()
    print("Created by Joyanta J. Mondal")
    print("Email: hello@joyantamondal.com")

def docs():
    print()
    print("======================================")
    print()
    print("add(course_name, course_cgpa, course_credits)")
    print("Add Course(s):")
    print("This method is to add course information.")
    print("There are three parameters to pass. Course Code (str), Course Grade (int/float), Course Credit Hours (int/float)")
    print()
    print("======================================")
    print()
    print("remove(course_name)")
    print("Remove Course(s):")
    print("This method is to remove course information.")
    print("There is one parameter to pass. Course Code (str)")
    print()
    print("======================================")
    print()
    print("======================================")
    print()
    print("check_attempted_course()")
    print("This method is to check courses attempted which were inputted.")
    print()
    print("======================================")
    print()
    print("get_cgpa()")
    print("Get CGPA:")
    print("This method is to check the CGPA with inputted courses.")
    print()
    print("======================================")
    print()
    print("credits_completed()")
    print("Credits Completed:")
    print("This method is to check amount of credits completed.")
    print()
    print("======================================")

    

