# BracU CGPA Calculator Module

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 

BracU CGPA Module is a Python library for easier calculation of CGPA in [Brac University](https://www.bracu.ac.bd/). 

Developed by [Joyanta J. Mondal](https://github.com/lepotatoguy) from BracU (C) 2021

Email: hello@joyantamondal.com

## Functionality:

- Adding Courses
- Removing Courses
- Checking Courses Attempted 
- Get CGPA
- Number of Credits Attempted
- Read from Device (PC/Google Colab)
- Save to Device (PC/Google Colab)

- Template of Excel File (Read from PC)
![Template of Excel File (Read from PC)](https://i.postimg.cc/1R7q78nt/getfrompc.png)

- Flush Info
- Check Completed Course. 
- Check Retake Course. 
- Credits Completed.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install bracu_cgpa_calc.

```
pip install bracu_cgpa_calc
```



## Usage

```python
from bracu_cgpa_calc import *
#import bracu_cgpa_calc as bcc #this is another alternative import

add("CSE110", 4, 3) #adding courses
add("CSE111", 3.7, 3) #adding courses
add("CSE220", 3.3, 3) #adding courses
add("MAT215", 0, 3) #adding courses
#bcc.add("MAT215", 0, 3) #adding courses using alternative import
remove("CSE220") #removing courses
check_attempted_course() #returns list of courses attempted.
check_completed_course() #returns list of courses completed.
check_retake_course() #returns list of courses needs retake.
credits_attempted() #returns number of credits attempted.
credits_completed() #returns number of credits completed.
get_cgpa() #returns CGPA
readme() #prints out readme
docs() #prints out documentation
save_to_pc() #self-explanatory
read_from_pc("CGPA.xlsx") #reads "CGPA.xlsx" from device
flush() #flushes all the data of course list and CGPA and everything from the code
```
## Note 
- I have tried to implement all the functionalities, it might have some bugs also. Please ignore that or please contact me email to notify me about the bug. I will try to give proper credits to that too. And you are welcome to give your valuable opinion and suggestions.

## License
[MIT](https://choosealicense.com/licenses/mit/)


## CHANGELOG:

1.0.6:
- Fixed: Course Remove was not working. 
- Fixed: Get CGPA was not working. 

1.0.5:
- Fixed: Credits Attempted was not adding number of credits. 
- Fixed: Flush was not removing Credits Completed. 

1.0.4:
- Added: Check Completed Course. 
- Added: Check Retake Course. 
- Added: Credits Completed.

1.0.3:
- Added: Flush.

1.0.2:
- Added: Save to Device. (Tested on PC and Google Colab)
- Added: Read from Device. (Tested on PC and Google Colab)

1.0.1:
- Fixed: Removing Courses: Wrong course was getting removed.
- Fixed: Checking Courses Attempted: It was showing random course instead of a list.

1.0.0:

- Added: Adding Courses
- Added: Removing Courses
- Added: Checking Courses Attempted 
- Added: Get CGPA
- Added: Number of Credits Attempted