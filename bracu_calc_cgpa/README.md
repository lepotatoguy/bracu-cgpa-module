# BracU CGPA Module

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 

BracU CGPA Module is a Python library for easier calculation of CGPA in BRACU.

Developed by Joyanta J. Mondal from BracU (C) 2021

Email: hello@joyantamondal.com

## Functionality of the module

- Adding Courses
- Removing Courses
- Checking Courses Attempted 
- Get CGPA
- Number of Credits Completed


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install bracu_calc_cgpa.

```bash
pip install bracu_calc_cgpa
```

## Usage

```python
from bracu_calc_cgpa import *

add("CSE110", 4, 3) #adding courses
add("CSE111", 3.7, 3) #adding courses
add("CSE220", 3.3, 3) #adding courses
add("MAT215", 0, 3) #adding courses
remove("CSE220") #adding courses
check_attempted_course() #returns list of courses attempted.
credits_completed() #returns number of credits completed.
get_cgpa() #returns CGPA

```
## Note 
- I have tried to implement all the functionalities, it might have some bugs also. Ignore that or please contact me email to notify me about the bug. I will try to give proper credits to that too. 

## License
[MIT](https://choosealicense.com/licenses/mit/)