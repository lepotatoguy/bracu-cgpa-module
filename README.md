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
- Read from PC
- Save to PC/GOogle Colab

- Template of Excel File (Read from PC)
![Template of Excel File (Read from PC)](https://i.postimg.cc/1R7q78nt/getfrompc.png)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install bracu_cgpa_calc.

```
pip install bracu_cgpa_calc
```



## Usage

```python
from bracu_cgpa_calc import *

add("CSE110", 4, 3) #adding courses
add("CSE111", 3.7, 3) #adding courses
add("CSE220", 3.3, 3) #adding courses
add("MAT215", 0, 3) #adding courses
remove("CSE220") #removing courses
check_attempted_course() #returns list of courses attempted.
credits_attempted() #returns number of credits completed.
get_cgpa() #returns CGPA
readme() #prints out readme
docs() #prints out documentation
save_to_pc() #Works in Google Colab too. 
read_from_pc("CGPA.xlsx")
```
## Note 
- I have tried to implement all the functionalities, it might have some bugs also. Please ignore that or please contact me email to notify me about the bug. I will try to give proper credits to that too. And you are welcome to give your valuable opinion and suggestions.

## License
[MIT](https://choosealicense.com/licenses/mit/)


## CHANGELOG:

1.0.2:
- Added: Save to PC.
- Added: Read from PC.

1.0.1:
- Fixed: Removing Courses: Wrong course was getting removed.
- Fixed: Checking Courses Attempted: It was showing random course instead of a list.

1.0.0:

- Adding Courses
- Removing Courses
- Checking Courses Attempted 
- Get CGPA
- Number of Credits Attempted