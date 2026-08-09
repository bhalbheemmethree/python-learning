# ==========================================================
# PYTHON DAY 14
# FUNCTIONS
# ==========================================================


# ==========================================================
# WHAT IS A FUNCTION?
# ==========================================================

# A function is a reusable block of code that performs
# a specific task.

# Instead of writing the same code again and again,
# we can write it once inside a function
# and call it whenever needed.


# ==========================================================
# WHY USE FUNCTIONS?
# ==========================================================

# Functions help to:

# - Reuse code
# - Reduce code repetition
# - Organize programs
# - Make code easier to understand
# - Make debugging easier


# ==========================================================
# DEFINING A FUNCTION
# ==========================================================

# A function is defined using the def keyword.

# Syntax:

# def function_name():
#     code


def greet():
    print("Hello!")

# The function is created here,
# but it has not executed yet.


# ==========================================================
# CALLING A FUNCTION
# ==========================================================

def greet():
    print("Hello!")

greet()

# Output

# Hello!

# Writing greet() calls the function
# and executes its code.


# ==========================================================
# FUNCTION CAN BE CALLED MULTIPLE TIMES
# ==========================================================

def greet():
    print("Hello!")

greet()
greet()
greet()

# Output

# Hello!
# Hello!
# Hello!

# A function can be reused multiple times.


# ==========================================================
# FUNCTION WITH MULTIPLE STATEMENTS
# ==========================================================

def welcome():
    print("Welcome to Python")
    print("Start learning")
    print("Keep practicing")

welcome()

# Output

# Welcome to Python
# Start learning
# Keep practicing


# ==========================================================
# FUNCTION NAME
# ==========================================================

# Function names should describe what the function does.

def calculate():
    print("Calculating...")

calculate()

# Good function names:

# calculate()
# login()
# display_menu()
# save_data()


# ==========================================================
# FUNCTION WITH NO ARGUMENTS
# ==========================================================

# A function can be created without receiving
# any values from outside.

def show_message():
    print("Python is easy")

show_message()

# Output

# Python is easy


# ==========================================================
# FUNCTION EXECUTION FLOW
# ==========================================================

def greet():
    print("Hello")

print("Before function")

greet()

print("After function")

# Output

# Before function
# Hello
# After function

# Python executes the function only when
# the function is called.


# ==========================================================
# FUNCTION DEFINITION VS FUNCTION CALL
# ==========================================================

def greet():
    print("Hello")

# Function definition:
# Creates the function.

greet()

# Function call:
# Executes the function.


# ==========================================================
# INDENTATION IN FUNCTIONS
# ==========================================================

def greet():
    print("Hello")
    print("Welcome")

greet()

# The indented statements belong to the function.


# ==========================================================
# FUNCTION WITH CONDITIONAL STATEMENT
# ==========================================================

def check_number():
    number = 10

    if number > 0:
        print("Positive")

check_number()

# Output

# Positive

# Functions can contain other Python statements.


# ==========================================================
# FUNCTION WITH A LOOP
# ==========================================================

def print_numbers():
    for i in range(1, 4):
        print(i)

print_numbers()

# Output

# 1
# 2
# 3

# Functions can contain loops as well.


# ==========================================================
# LOCAL VARIABLES
# ==========================================================

def show_name():
    name = "Bhalbheem"
    print(name)

show_name()

# name is created inside the function.
# It is a local variable.


# ==========================================================
# LOCAL SCOPE
# ==========================================================

def example():
    message = "Hello"
    print(message)

example()

# message exists inside the function's local scope.

# It cannot normally be accessed outside the function.

# Example:

# print(message)   # Error


# ==========================================================
# FUNCTIONS HELP ORGANIZE CODE
# ==========================================================

def login():
    print("Login process")

def logout():
    print("Logout process")

login()
logout()

# Output

# Login process
# Logout process

# Large programs can be divided into
# smaller functions.


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# def -> Used to define a function.

# Function definition -> Creates the function.

# Function call -> Executes the function.

# A function can be called multiple times.

# A function can contain multiple statements.

# Indentation defines the function body.

# Functions improve code reuse and organization.

# A function can exist without arguments.

# Local variables are created inside a function
# and belong to that function's local scope.
