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


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install bracucgpacalc.

```
pip install bracucgpacalc
```
Or,



## Usage

```python
from bracucgpacalc import *

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

```
## Note 
- I have tried to implement all the functionalities, it might have some bugs also. Please ignore that or please contact me email to notify me about the bug. I will try to give proper credits to that too. 

## License
[MIT](https://choosealicense.com/licenses/mit/)