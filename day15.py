# ==========================================================
# PYTHON DAY 15
# FUNCTION ARGUMENTS & RETURN STATEMENT
# ==========================================================


# ==========================================================
# FUNCTION ARGUMENTS
# ==========================================================

# Arguments are values passed to a function
# when the function is called.

def greet(name):
    print("Hello", name)

greet("Bhalbheem")

# Output

# Hello Bhalbheem


# ==========================================================
# PARAMETERS VS ARGUMENTS
# ==========================================================

def greet(name):
    print("Hello", name)

# name is a parameter.

greet("Bhalbheem")

# "Bhalbheem" is an argument.

# Parameter -> Variable defined in the function.
# Argument  -> Actual value passed to the function.


# ==========================================================
# FUNCTION WITH MULTIPLE PARAMETERS
# ==========================================================

def add(a, b):
    print(a + b)

add(10, 20)

# Output

# 30

# a and b are parameters.
# 10 and 20 are arguments.


# ==========================================================
# POSITIONAL ARGUMENTS
# ==========================================================

def student(name, age):
    print(name)
    print(age)

student("Bhalbheem", 17)

# Output

# Bhalbheem
# 17

# Values are assigned according to their position.

# "Bhalbheem" -> name
# 17           -> age


# ==========================================================
# KEYWORD ARGUMENTS
# ==========================================================

def student(name, age):
    print(name)
    print(age)

student(age=17, name="Bhalbheem")

# Output

# Bhalbheem
# 17

# Keyword arguments specify the parameter name,
# so their order does not matter.


# ==========================================================
# DEFAULT ARGUMENTS
# ==========================================================

def greet(name="User"):
    print("Hello", name)

greet()

# Output

# Hello User

greet("Bhalbheem")

# Output

# Hello Bhalbheem

# A default argument is used when no value
# is provided for that parameter.


# ==========================================================
# MULTIPLE DEFAULT ARGUMENTS
# ==========================================================

def student(name="Unknown", age=0):
    print(name)
    print(age)

student()

# Output

# Unknown
# 0


# ==========================================================
# ARGUMENT + DEFAULT ARGUMENT
# ==========================================================

def greet(name, message="Hello"):
    print(message, name)

greet("Bhalbheem")

# Output

# Hello Bhalbheem

greet("Bhalbheem", "Welcome")

# Output

# Welcome Bhalbheem


# ==========================================================
# RETURN STATEMENT
# ==========================================================

# return sends a value back from a function.

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

# Output

# 30


# ==========================================================
# return VS print
# ==========================================================

def add(a, b):
    print(a + b)

add(10, 20)

# print() displays the result,
# but does not send the value back to the caller.


def add(a, b):
    return a + b

result = add(10, 20)

print(result)

# return allows us to store and use
# the returned value.


# ==========================================================
# USING RETURNED VALUE
# ==========================================================

def add(a, b):
    return a + b

result = add(10, 20)

print(result * 2)

# Output

# 60

# The returned value can be used in other operations.


# ==========================================================
# RETURN STOPS FUNCTION EXECUTION
# ==========================================================

def check():
    print("Before return")

    return

    print("After return")

check()

# Output

# Before return

# Code after return is not executed.


# ==========================================================
# RETURNING A VALUE
# ==========================================================

def square(number):
    return number * number

result = square(5)

print(result)

# Output

# 25


# ==========================================================
# FUNCTION WITH ARGUMENTS AND RETURN
# ==========================================================

def multiply(a, b):
    return a * b

result = multiply(5, 4)

print(result)

# Output

# 20

# Arguments provide data to the function.
# return sends the result back.


# ==========================================================
# RETURNING MULTIPLE VALUES
# ==========================================================

def calculate(a, b):
    return a + b, a - b

result = calculate(10, 5)

print(result)

# Output

# (15, 5)

# Python can return multiple values.
# They are returned together as a tuple.


# ==========================================================
# RETURNING MULTIPLE VALUES INTO VARIABLES
# ==========================================================

def calculate(a, b):
    return a + b, a - b

addition, subtraction = calculate(10, 5)

print(addition)
print(subtraction)

# Output

# 15
# 5


# ==========================================================
# FUNCTION WITHOUT RETURN
# ==========================================================

def greet():
    print("Hello")

result = greet()

print(result)

# Output

# Hello
# None

# If a function does not explicitly return a value,
# Python returns None.


# ==========================================================
# RETURNING NONE
# ==========================================================

def test():
    return

result = test()

print(result)

# Output

# None


# ==========================================================
# ARGUMENTS + if + RETURN
# ==========================================================

def check_age(age):

    if age >= 18:
        return "Eligible"

    return "Not eligible"

result = check_age(20)

print(result)

# Output

# Eligible


# ==========================================================
# ARGUMENTS + LOOP + RETURN
# ==========================================================

def find_number(numbers, target):

    for number in numbers:

        if number == target:
            return True

    return False


numbers = [10, 20, 30, 40]

print(find_number(numbers, 30))

# Output

# True
