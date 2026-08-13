# ==========================================================
# PYTHON DAY 28
# EXCEPTION HANDLING
# ==========================================================


# ==========================================================
# WHAT IS AN EXCEPTION?
# ==========================================================

# Definition

'''An exception is an error that occurs during the execution
of a program and interrupts its normal flow.'''

# Example

number = 10
result = number / 0

print(result)

# Output:

# ZeroDivisionError

# Division by zero causes an exception.


# ==========================================================
# WHY IS EXCEPTION HANDLING NEEDED?
# ==========================================================

'''Exception handling allows us to handle errors without
crashing the entire program.

It helps the program continue or display a meaningful
error message.'''


# ==========================================================
# try AND except
# ==========================================================

# The try block contains code that may cause an exception.

# The except block handles the exception.

# Syntax:

# try:

    # Code that may cause an exception

# except:

    # Code to handle the exception


# ==========================================================
# BASIC EXAMPLE
# ==========================================================

# try:

number = 10 / 0

# except:

print("An error occurred")

# Output:

# An error occurred


# ==========================================================
# HANDLING A SPECIFIC EXCEPTION
# ==========================================================

try:

    number = 10 / 0

except ZeroDivisionError:

    print("Cannot divide by zero")

# Output:

# Cannot divide by zero


# ==========================================================
# VALUEERROR
# ==========================================================

# ValueError occurs when a function receives
# an inappropriate value.

try:

    age = int("hello")

except ValueError:

    print("Invalid value")

# Output:

# Invalid value


# ==========================================================
# TYPEERROR
# ==========================================================

# TypeError occurs when an operation is performed
# on incompatible data types.

try:

    result = 10 + "5"

except TypeError:

    print("Cannot add integer and string")

# Output:

# Cannot add integer and string


# ==========================================================
# NAMEERROR
# ==========================================================

# NameError occurs when a variable or name
# is not defined.

try:

    print(age)

except NameError:

    print("Variable is not defined")

# Output:

# Variable is not defined


# ==========================================================
# INDEXERROR
# ==========================================================

# IndexError occurs when trying to access
# an index that does not exist.

numbers = [10, 20, 30]

try:

    print(numbers[5])

except IndexError:

    print("Index does not exist")

# Output:

# Index does not exist


# ==========================================================
# KEYERROR
# ==========================================================

# KeyError occurs when trying to access
# a dictionary key that does not exist.

student = {
    "name": "Bhalbheem",
    "age": 18
}

try:

    print(student["branch"])

except KeyError:

    print("Key does not exist")

# Output:

# Key does not exist


# ==========================================================
# MULTIPLE EXCEPT BLOCKS
# ==========================================================

# Multiple except blocks can be used
# to handle different exceptions.

try:

    number = int(input("Enter a number: "))
    result = 10 / number

except ValueError:

    print("Please enter a valid number")

except ZeroDivisionError:

    print("Cannot divide by zero")


# ==========================================================
# EXCEPT WITHOUT SPECIFYING EXCEPTION
# ==========================================================

try:

    number = 10 / 0

except:

    print("Something went wrong")

# This handles the exception,
# but using a specific exception is generally clearer.


# ==========================================================
# AS KEYWORD
# ==========================================================

# The 'as' keyword allows us to store
# the exception object in a variable.

try:

    number = 10 / 0

except ZeroDivisionError as error:

    print(error)

# Output:

# division by zero


# ==========================================================
# EXCEPTION OBJECT
# ==========================================================

try:

    number = int("hello")

except ValueError as error:

    print("Error:", error)

# Output:

# Error: invalid literal for int() with base 10: 'hello'


# ==========================================================
# TRY WITH SUCCESSFUL CODE
# ==========================================================

try:

    number = 10 / 2

except ZeroDivisionError:

    print("Cannot divide by zero")

print("Program continues")

# Output:

# Program continues

# If no exception occurs,
# the except block is skipped.


# ==========================================================
# TRY WITH EXCEPTION
# ==========================================================

try:

    number = 10 / 0

except ZeroDivisionError:

    print("Cannot divide by zero")

print("Program continues")

# Output:

# Cannot divide by zero
# Program continues


# ==========================================================
# EXCEPTION HANDLING WITH USER INPUT
# ==========================================================

try:

    age = int(input("Enter your age: "))

    print("Your age is:", age)

except ValueError:

    print("Please enter a valid integer")

# If the user enters:

# 18

# Output:

# Your age is: 18

# If the user enters:

# abc

# Output:

# Please enter a valid integer


# ==========================================================
# EXCEPTION HANDLING IN A CALCULATION
# ==========================================================

try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ValueError:

    print("Please enter numbers only")

except ZeroDivisionError:

    print("Cannot divide by zero")


# ==========================================================
# COMMON PYTHON EXCEPTIONS
# ==========================================================

# ZeroDivisionError
# -> Division by zero.

# ValueError
# -> Invalid value.

# TypeError
# -> Incompatible data types.

# NameError
# -> Name or variable is not defined.

# IndexError
# -> Invalid list/sequence index.

# KeyError
# -> Dictionary key does not exist.

# FileNotFoundError
# -> Requested file does not exist.


# ==========================================================
# EXCEPTION HANDLING FLOW
# ==========================================================

# try:

    # Risky code

# except:

    # Handle exception


# Flow:

# Program starts
#      ↓
# try block executes
#      ↓
# Exception occurs?
#      ↓
# YES → except block executes
#      ↓
# Program continues


# If no exception:

# Program starts
#      ↓
# try block executes
#      ↓
# No exception
#      ↓
# except is skipped
#      ↓
# Program continues


# ==========================================================
# IMPORTANT POINT
# ==========================================================

# Exception handling does NOT mean
# that errors are ignored.

# It means the program handles
# unexpected situations properly.


# ==========================================================
# EXCEPTION VS SYNTAX ERROR
# ==========================================================

# Syntax Error:

# Occurs when Python code does not follow
# the correct syntax.

# Example:

# if True
#     print("Hello")

# This produces a SyntaxError.


# Exception:

# Usually occurs while the program is running.

# Example:

# number = 10 / 0

# This produces ZeroDivisionError.


# ==========================================================
# QUICK REVISION
# ==========================================================

# try
# -> Contains code that may cause an exception.

# except
# -> Handles the exception.

# as
# -> Stores the exception object.


# ==========================================================
# SUMMARY
# ==========================================================
#  An exception is an error that occurs during execution.
# • Exception handling prevents unexpected crashes.
# • try contains potentially risky code.
# • except handles exceptions.
# • Specific exceptions can be handled separately.
# • Multiple except blocks can be used.
# • The 'as' keyword can store the exception object.
# • Common exceptions include ValueError, TypeError,
#  ZeroDivisionError, IndexError, KeyError and NameError.