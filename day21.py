# ==========================================================
# PYTHON DAY 21
# DOCSTRINGS & PEP 8
# ==========================================================


# ==========================================================
# DOCSTRINGS
# ==========================================================

# A docstring is a string used to describe
# what a function, class, or module does.

# Docstrings are usually written using
# triple quotes.


# ==========================================================
# FUNCTION DOCSTRING
# ==========================================================

def greet():
    """This function prints a greeting message."""
    print("Hello!")

greet()


# ==========================================================
# ACCESSING A DOCSTRING
# ==========================================================

def greet():
    """This function prints a greeting message."""
    print("Hello!")

print(greet.__doc__)

# Output

# This function prints a greeting message.


# ==========================================================
# MULTI-LINE DOCSTRING
# ==========================================================

def student_info():
    """
    This function displays
    student information.
    """
    print("Name: Bhalbheem")
    print("Branch: CSE")

student_info()


# ==========================================================
# DOCSTRING VS COMMENT
# ==========================================================

# Comment:

# This function prints a greeting.

def greet():
    print("Hello")


# Docstring:

def greet():
    """This function prints a greeting."""
    print("Hello")


# Main difference:

# Comment -> Helps developers understand the code.

# Docstring -> Documents a function, class, or module
#              and can be accessed using __doc__.


# ==========================================================
# DOCSTRING MUST BE INSIDE THE FUNCTION
# ==========================================================

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add.__doc__)

# Output

# Returns the sum of two numbers.


# ==========================================================
# MODULE DOCSTRING
# ==========================================================

"""
This module contains basic
mathematical functions.
"""

# A module-level docstring describes
# the purpose of the Python file.


# ==========================================================
# PEP 8 (Python Enhancement Proposal 8)
# ==========================================================

# PEP 8 is the official Python style guide.

# It provides recommendations for writing
# clean, readable, and consistent Python code.


# ==========================================================
# INDENTATION
# ==========================================================

# Python uses 4 spaces for indentation.

def greet():
    print("Hello")
    print("Welcome")


# Avoid unnecessary or inconsistent indentation.


# ==========================================================
# VARIABLE NAMING
# ==========================================================

# Use lowercase letters with underscores
# for variable names.

student_name = "Bhalbheem"
student_age = 17


# Avoid:

# StudentName = "Bhalbheem"
# studentAge = 17

# For normal variables, snake_case is preferred.


# ==========================================================
# FUNCTION NAMING
# ==========================================================

# Functions should also use snake_case.

def calculate_total():
    pass


def display_student():
    pass


# ==========================================================
# CONSTANT NAMING
# ==========================================================

# Constants are generally written
# using uppercase letters.

PI = 3.14159
MAX_SIZE = 100


# ==========================================================
# SPACES AROUND OPERATORS
# ==========================================================

# Good:

# total = price + tax
# result = a * b


# Avoid:

# total=price+tax
# result=a*b


# ==========================================================
# SPACES AFTER COMMAS
# ==========================================================

# Good:

numbers = [10, 20, 30, 40]


# Avoid:

# numbers = [10,20,30,40]


# ==========================================================
# BLANK LINES
# ==========================================================

# Use blank lines to separate
# logically different sections of code.

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# ==========================================================
# LINE LENGTH
# ==========================================================

# PEP 8 recommends keeping lines reasonably short,
# traditionally around 79 characters for code.


# Instead of writing one extremely long line,
# break it into multiple lines.

message = (
    "This is a long message that "
    "has been split across multiple lines."
)


# ==========================================================
# IMPORTS
# ==========================================================

# Imports should generally be placed
# at the beginning of the file.

import math

print(math.sqrt(25))


# ==========================================================
# COMMENTS
# ==========================================================

# Write comments that explain something useful.

# Calculate the total price after applying the discount.
### total = price - discount


# Avoid comments that simply repeat the code.

# Add 10 to x
### x = x + 10


# ==========================================================
# COMPARISON OF GOOD AND BAD STYLE
# ==========================================================

# Bad:

# x=10
# y=20
# z=x+y
# print(z)


# Good:

x = 10
y = 20
z = x + y

print(z)


# ==========================================================
# PEP 8 NAMING SUMMARY
# ==========================================================

# Variables:
# snake_case

student_name = "Bhalbheem"


# Functions:
# snake_case

def calculate_total():
    pass


# Constants:
# UPPER_CASE

MAX_VALUE = 100


# Classes:
# PascalCase
#
# Classes will be covered later.


# ==========================================================
# WHY PEP 8?
# ==========================================================

# PEP 8 helps make code:

# - Readable
# - Consistent
# - Easier to maintain
# - Easier for other developers to understand


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# Docstring -> Documents code.

# Docstrings are commonly written using
# triple quotes.

# __doc__ -> Accesses a docstring.

# PEP 8 -> Python style guide.

# Use 4 spaces for indentation.

# Use snake_case for normal variables and functions.

# Use UPPER_CASE for constants.

# Use spaces around operators.

# Use spaces after commas.

# Use blank lines to separate logical sections.

# Keep code lines reasonably short.

# Keep imports organized near the beginning of the file.


# ==========================================================
# QUICK REVISION
# ==========================================================

def calculate_area(length, width):
    """Returns the area of a rectangle."""
    return length * width

length = 10
width = 5

area = calculate_area(length, width)

print(area)
print(calculate_area.__doc__)
