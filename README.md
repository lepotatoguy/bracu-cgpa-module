# BracU CGPA Module

BracU CGPA Module is a Python library for easier calculation of CGPA in BRACU.

Developed by Joyanta J. Mondal from BracU (c) 2021

Email: hello@joyantamondal.com

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cgpa_bracu.

```bash
pip install cgpa_bracu
```

## Usage

```python
import cgpa_bracu

add("CSE110", 4, 3) #adding courses
add("CSE111", 3.7, 3) #adding courses
add("CSE220", 3.3, 3) #adding courses
add("MAT215", 0, 3) #adding courses
remove("CSE220") #adding courses
check_course_done() #returns list of courses inputted.
credits_completed() #returns number of credits completed.
get_cgpa() #returns CGPA

```

## License
[MIT](https://choosealicense.com/licenses/mit/)