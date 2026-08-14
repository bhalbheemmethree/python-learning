# ==========================================================
# PYTHON DAY 37
# LOCAL AND GLOBAL VARIABLES
# ==========================================================


# ==========================================================
# WHAT IS A VARIABLE SCOPE?
# ==========================================================

# Definition:

# Variable scope refers to the part of a program where
# a variable can be accessed.


# ==========================================================
# LOCAL VARIABLE
# ==========================================================

# Definition:

# A local variable is a variable created inside a function
# and can normally be accessed only inside that function.

# Example:

def greet():

    name = "Bhalbheem"

    print(name)


greet()

# Output:

# Bhalbheem

# name is a local variable of greet().


# ==========================================================
# LOCAL VARIABLE CANNOT NORMALLY BE ACCESSED OUTSIDE
# ==========================================================

def greet():

    name = "Bhalbheem"


greet()

# print(name)

# This causes:

# NameError

# Because name exists only inside greet().


# ==========================================================
# GLOBAL VARIABLE
# ==========================================================

# Definition:

# A global variable is a variable created outside functions
# and can be accessed from different parts of the program.

# Example:

name = "Bhalbheem"


def greet():

    print(name)


greet()

# Output:

# Bhalbheem


# ==========================================================
# GLOBAL VARIABLE OUTSIDE FUNCTION
# ==========================================================

name = "Bhalbheem"

print(name)

# Output:

# Bhalbheem


# ==========================================================
# LOCAL VS GLOBAL VARIABLE
# ==========================================================

name = "Global"


def example():

    name = "Local"

    print(name)


example()

print(name)

# Output:

# Local
# Global

# The local variable is used inside the function.
# The global variable remains unchanged outside.


# ==========================================================
# SAME VARIABLE NAME
# ==========================================================

x = 10


def example():

    x = 20

    print("Inside:", x)


example()

print("Outside:", x)

# Output:

# Inside: 20
# Outside: 10

# The x inside the function is a local variable.


# ==========================================================
# ACCESSING GLOBAL VARIABLE INSIDE FUNCTION
# ==========================================================

x = 10


def example():

    print(x)


example()

# Output:

# 10

# A function can read a global variable.


# ==========================================================
# MODIFYING A GLOBAL VARIABLE
# ==========================================================

x = 10


def change():

    global x

    x = 20


change()

print(x)

# Output:

# 20

# The global keyword allows the function
# to modify the global variable.


# ==========================================================
# global KEYWORD
# ==========================================================

# Definition:

# The global keyword tells Python that a variable inside
# a function refers to the global variable.

# Syntax:

global variable_name


# ==========================================================
# EXAMPLE OF global
# ==========================================================

count = 0


def increase():

    global count

    count += 1


increase()
increase()

print(count)

# Output:

# 2


# ==========================================================
# WITHOUT global
# ==========================================================

count = 0


def increase():

    count += 1


increase()

# This causes:

# UnboundLocalError

# Python treats count as a local variable because
# the function attempts to assign to it.


# ==========================================================
# LOCAL VARIABLE WITH global VARIABLE
# ==========================================================

x = 100


def example():

    x = 50

    print(x)


example()

print(x)

# Output:

# 50
# 100


# ==========================================================
# GLOBAL KEYWORD WITH DIFFERENT VARIABLE
# ==========================================================

x = 100


def example():

    global x

    x = 50


example()

print(x)

# Output:

# 50


# ==========================================================
# GLOBAL VARIABLES IN MULTIPLE FUNCTIONS
# ==========================================================

score = 0


def add_score():

    global score

    score += 10


def show_score():

    print(score)


add_score()
add_score()

show_score()

# Output:

# 20


# ==========================================================
# LOCAL VARIABLE IN MULTIPLE FUNCTIONS
# ==========================================================

def first():

    x = 10

    print(x)


def second():

    x = 20

    print(x)


first()
second()

# Output:

# 10
# 20

# Each function has its own local x.


# ==========================================================
# GLOBAL CONSTANTS
# ==========================================================

# Definition:

# A global constant is a value defined at the top level
# that is intended not to change.

# Python commonly uses uppercase names for constants.

# Example:

PI = 3.14159
MAX_SIZE = 100

# These are conventions.
# Python does not strictly prevent them from being changed.


# ==========================================================
# IMPORTANT POINT
# ==========================================================

# Global variables can be read inside functions.

x = 10


def show():

    print(x)


show()


# To modify a global variable inside a function,
# use global.

x = 10


def change():

    global x

    x = 20


# ==========================================================
# LOCAL AND GLOBAL — QUICK COMPARISON
# ==========================================================

# Local Variable:

# • Created inside a function.
# • Normally accessible only inside that function.
# • Exists within its local scope.


# Global Variable:

# • Created outside functions.
# • Can be accessed from different parts of the program.
# • Can be modified inside a function using global.


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# • Scope determines where a variable can be accessed.
# • Variables created inside functions are local by default.
# • Variables created outside functions are global.
# • A function can read a global variable.
# • The global keyword allows modification of a global variable.
# • Local variables with the same name as global variables
#   are separate variables.
# • Excessive use of global variables can make programs
#   harder to maintain.


# ==========================================================
# QUICK REVISION
# ==========================================================

x = 10


def example():

    print(x)


# x is global.


def test():

    y = 20

    print(y)


# y is local.


# To modify x:

def change():

    global x

    x = 50


# ==========================================================
# SUMMARY
# ==========================================================

# • Local variables belong to a function's local scope.
# • Global variables are defined outside functions.
# • Global variables can be read inside functions.
# • The global keyword allows modification of global variables.
# • A local variable can have the same name as a global variable.
# • Understanding scope prevents variable-access errors.
