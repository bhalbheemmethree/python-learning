# ==========================================================
# PYTHON DAY 30
# RAISING CUSTOM ERRORS
# ==========================================================


# ==========================================================
# WHAT IS RAISING AN ERROR?
# ==========================================================

# Definition:

'''The raise statement is used to manually raise an exception
when a specific condition occurs.

Python normally raises exceptions automatically when an
error occurs, but we can also raise them ourselves.'''


# ==========================================================
# BASIC SYNTAX
# ==========================================================

# raise ExceptionType("Error message")


# ==========================================================
# BASIC EXAMPLE
# ==========================================================

age = 15

if age < 18:

    raise ValueError("Age must be 18 or above")

# Output:

# ValueError: Age must be 18 or above


# ==========================================================
# RAISING VALUEERROR
# ==========================================================

number = -5

if number < 0:

    raise ValueError("Number cannot be negative")

print(number)

# The program stops when the exception is raised.


# ==========================================================
# RAISING TYPEERROR
# ==========================================================

name = 123

if not isinstance(name, str):

    raise TypeError("Name must be a string")

# Output:

# TypeError: Name must be a string


# ==========================================================
# RAISING AN ERROR WITH USER INPUT
# ==========================================================

age = int(input("Enter your age: "))

if age < 0:

    raise ValueError("Age cannot be negative")

print("Age:", age)


# ==========================================================
# USING raise WITH try AND except
# ==========================================================

try:

    age = int(input("Enter your age: "))

    if age < 18:

        raise ValueError("You must be 18 or above")

    print("Eligible")

except ValueError as error:

    print("Error:", error)


# ==========================================================
# CUSTOM VALIDATION
# ==========================================================

marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:

    raise ValueError("Marks must be between 0 and 100")

print("Marks:", marks)


# ==========================================================
# CUSTOM ERROR MESSAGE
# ==========================================================

password = input("Enter password: ")

if len(password) < 8:

    raise ValueError("Password must contain at least 8 characters")

print("Password accepted")


# ==========================================================
# CREATING A CUSTOM EXCEPTION CLASS
# ==========================================================

# Definition:

'''A custom exception is a user-defined exception created
by inheriting from the Exception class.'''

# Example:

class AgeError(Exception):

    pass


age = 15

if age < 18:

    raise AgeError("Age must be 18 or above")


# ==========================================================
# HANDLING A CUSTOM EXCEPTION
# ==========================================================

class AgeError(Exception):

    pass


try:

    age = 15

    if age < 18:

        raise AgeError("Age must be 18 or above")

except AgeError as error:

    print("Error:", error)

# Output:

# Error: Age must be 18 or above


# ==========================================================
# CUSTOM EXCEPTION WITH USER INPUT
# ==========================================================

class InvalidMarksError(Exception):

    pass


try:

    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:

        raise InvalidMarksError("Marks must be between 0 and 100")

    print("Valid marks")

except InvalidMarksError as error:

    print("Error:", error)


# ==========================================================
# CUSTOM EXCEPTION WITH FUNCTION
# ==========================================================

class InsufficientBalanceError(Exception):

    pass


def withdraw(balance, amount):

    if amount > balance:

        raise InsufficientBalanceError(
            "Insufficient balance"
        )

    return balance - amount


try:

    balance = 5000

    balance = withdraw(balance, 6000)

    print("Remaining balance:", balance)

except InsufficientBalanceError as error:

    print("Error:", error)

# Output:

# Error: Insufficient balance


# ==========================================================
# WHY USE CUSTOM EXCEPTIONS?
# ==========================================================

'''Custom exceptions allow us to create meaningful errors
for specific situations in our programs.'''

# For example:

# • Invalid age
# • Invalid marks
# • Insufficient balance
# • Invalid username
# • Invalid password
# • Insufficient stock


# ==========================================================
# raise VS except
# ==========================================================

# raise:

# Used to manually create/raise an exception.

# Example:

raise ValueError("Invalid value")


# except:

# Used to handle an exception.

# Example:

try:

    raise ValueError("Invalid value")

except ValueError:

    print("Error handled")


# ==========================================================
# raise WITH EXISTING EXCEPTION
# ==========================================================

try:

    number = int("abc")

except ValueError:

    print("Invalid number")
    raise

# The raise statement without an exception
# re-raises the current exception.


# ==========================================================
# IMPORTANT DIFFERENCE
# ==========================================================

# Python automatically raises errors:

number = 10 / 0

# Python raises ZeroDivisionError automatically.


# We can manually raise an error:

raise ValueError("Invalid value")

# We decide when the exception should occur.


# ==========================================================
# COMMON BUILT-IN EXCEPTIONS THAT CAN BE RAISED
# ==========================================================

raise ValueError("Invalid value")

raise TypeError("Invalid type")

raise RuntimeError("Runtime error")

raise IndexError("Invalid index")

raise KeyError("Invalid key")


# ==========================================================
# CUSTOM EXCEPTION SYNTAX
# ==========================================================

class MyError(Exception):

    pass


raise MyError("Something went wrong")


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# • raise is used to manually raise an exception.
# • raise can be used with built-in exceptions.
# • Custom exceptions can be created by inheriting
#   from the Exception class.
# • Custom exceptions make error messages more meaningful.
# • raise can be used inside try blocks.
# • Custom exceptions can be handled using except.


# ==========================================================
# QUICK REVISION
# ==========================================================

# raise
# -> Manually raises an exception.

# ValueError
# -> Commonly used for invalid values.

# TypeError
# -> Used when the data type is incorrect.

# Custom Exception
# -> User-defined exception created by inheriting
#    from Exception.


# ==========================================================
# SUMMARY
# ==========================================================

# • The raise statement manually raises exceptions.
# • It is useful for validating user input.
# • It allows programmers to create meaningful errors.
# • Custom exceptions can be created using Exception.
# • Custom exceptions are handled using try and except.
# • raise can also re-raise an existing exception.
