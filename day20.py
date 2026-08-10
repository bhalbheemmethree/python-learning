# ==========================================================
# PYTHON DAY 20
# f-STRINGS
# ==========================================================


# ==========================================================
# WHAT IS AN f-STRING?
# ==========================================================

# An f-string is a convenient way to insert
# variables and expressions directly into a string.

# f-strings are created by putting f before the string.

name = "Bhalbheem"

print(f"Hello {name}")

# Output

# Hello Bhalbheem


# ==========================================================
# BASIC SYNTAX
# ==========================================================

# Syntax:

# f"Text {variable}"


name = "Bhalbheem"
age = 17

print(f"My name is {name} and I am {age} years old.")

# Output

# My name is Bhalbheem and I am 17 years old.


# ==========================================================
# MULTIPLE VARIABLES
# ==========================================================

name = "Bhalbheem"
age = 17
branch = "CSE"

print(f"My name is {name}, I am {age}, and my branch is {branch}.")

# Output

# My name is Bhalbheem, I am 17, and my branch is CSE.


# ==========================================================
# EXPRESSIONS INSIDE f-STRINGS
# ==========================================================

a = 10
b = 20

print(f"Sum = {a + b}")

# Output

# Sum = 30

# Python evaluates the expression inside { }.


# ==========================================================
# MORE EXPRESSIONS
# ==========================================================

a = 10
b = 5

print(f"Addition = {a + b}")
print(f"Subtraction = {a - b}")
print(f"Multiplication = {a * b}")
print(f"Division = {a / b}")

# Output

# Addition = 15
# Subtraction = 5
# Multiplication = 50
# Division = 2.0


# ==========================================================
# EXPRESSIONS WITH VARIABLES
# ==========================================================

price = 100
quantity = 3

print(f"Total price = {price * quantity}")

# Output

# Total price = 300


# ==========================================================
# FUNCTION CALLS INSIDE f-STRINGS
# ==========================================================

name = "python"

print(f"Uppercase: {name.upper()}")

# Output

# Uppercase: PYTHON


# ==========================================================
# FLOAT VALUES
# ==========================================================

price = 99.99

print(f"The price is {price}")

# Output

# The price is 99.99


# ==========================================================
# FORMATTING DECIMAL PLACES
# ==========================================================

price = 99.9999

print(f"Price = {price:.2f}")

# Output

# Price = 100.00

# .2f means:
# Display the number with 2 digits after the decimal point.


# ==========================================================
# MORE DECIMAL FORMATTING
# ==========================================================

number = 12.345678

print(f"{number:.2f}")
print(f"{number:.3f}")

# Output

# 12.35
# 12.346


# ==========================================================
# PERCENTAGE FORMATTING
# ==========================================================

percentage = 0.85

print(f"Percentage = {percentage:.0%}")

# Output

# Percentage = 85%


# ==========================================================
# COMMA SEPARATOR FOR LARGE NUMBERS
# ==========================================================

number = 1000000

print(f"{number:,}")

# Output

# 1,000,000


# ==========================================================
# USING EXPRESSIONS WITH FORMATTING
# ==========================================================

price = 99.999

print(f"Total = {price * 2:.2f}")

# Output

# Total = 200.00


# ==========================================================
# f-STRING WITH BOOLEAN VALUES
# ==========================================================

is_student = True

print(f"Student: {is_student}")

# Output

# Student: True


# ==========================================================
# f-STRING WITH LISTS
# ==========================================================

names = ["Alice", "Bob", "Charlie"]

print(f"Students: {names}")

# Output

# Students: ['Alice', 'Bob', 'Charlie']


# ==========================================================
# ACCESSING LIST ELEMENTS
# ==========================================================

names = ["Alice", "Bob", "Charlie"]

print(f"First student: {names[0]}")

# Output

# First student: Alice


# ==========================================================
# f-STRING WITH DICTIONARY VALUES
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17
}

print(f"Name: {student['name']}")
print(f"Age: {student['age']}")

# Output

# Name: Bhalbheem
# Age: 17


# ==========================================================
# CALLING FUNCTIONS INSIDE f-STRINGS
# ==========================================================

def greet():
    return "Hello"

print(f"{greet()} Bhalbheem")

# Output

# Hello Bhalbheem


# ==========================================================
# USING CURLY BRACES AS NORMAL CHARACTERS
# ==========================================================

# In an f-string, { } are used for expressions.

# To display actual curly braces,
# use double curly braces.

name = "Bhalbheem"

print(f"{{name}} = {name}")

# Output

# {name} = Bhalbheem


# ==========================================================
# f-STRING VS NORMAL STRING
# ==========================================================

name = "Bhalbheem"

# Normal string:

print("Hello {name}")

# Output

# Hello {name}


# f-string:

print(f"Hello {name}")

# Output

# Hello Bhalbheem

# The f before the string allows Python
# to evaluate expressions inside { }.


# ==========================================================
# f-STRING WITH CALCULATIONS
# ==========================================================

length = 10
width = 5

print(f"Area = {length * width}")

# Output

# Area = 50


# ==========================================================
# f-STRING WITH CONDITIONAL EXPRESSION
# ==========================================================

age = 20

print(f"Status: {'Adult' if age >= 18 else 'Minor'}")

# Output

# Status: Adult


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# f-strings start with f before the string.

# Variables are placed inside { }.

# Expressions can be placed inside { }.

# Function calls can be placed inside { }.

# f-strings make string formatting easier and cleaner.

# :.2f formats a number to 2 decimal places.

# :,.2f can display large numbers with commas
# and 2 decimal places.

# Double {{ }} displays actual curly braces.


# ==========================================================
# QUICK REVISION
# ==========================================================

name = "Bhalbheem"
age = 17

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"Next year I will be {age + 1}")
