# ==========================================================
# PYTHON DAY 31
# SHORT-HAND IF-ELSE
# ==========================================================


# ==========================================================
# WHAT IS SHORT-HAND IF-ELSE?
# ==========================================================

# Definition:

'''Short-hand if-else is a single-line way of writing
a simple if-else statement.'''

# It is also called a conditional expression.


# ==========================================================
# NORMAL IF-ELSE
# ==========================================================

age = 18

if age >= 18:

    result = "Adult"

else:

    result = "Minor"

print(result)

# Output:

# Adult


# ==========================================================
# SHORT-HAND IF-ELSE
# ==========================================================

age = 18

result = "Adult" if age >= 18 else "Minor"

print(result)

# Output:

# Adult


# ==========================================================
# SYNTAX
# ==========================================================

# value_if_true if condition else value_if_false


# ==========================================================
# BASIC EXAMPLE
# ==========================================================

number = 10

result = "Positive" if number > 0 else "Not Positive"

print(result)

# Output:

# Positive


# ==========================================================
# EVEN OR ODD
# ==========================================================

number = 7

result = "Even" if number % 2 == 0 else "Odd"

print(result)

# Output:

# Odd


# ==========================================================
# CHECKING AGE
# ==========================================================

age = 20

status = "Eligible" if age >= 18 else "Not Eligible"

print(status)

# Output:

# Eligible


# ==========================================================
# COMPARING TWO NUMBERS
# ==========================================================

a = 10
b = 20

larger = a if a > b else b

print(larger)

# Output:

# 20


# ==========================================================
# CHECKING POSITIVE OR NEGATIVE
# ==========================================================

number = -5

result = "Positive" if number >= 0 else "Negative"

print(result)

# Output:

# Negative


# ==========================================================
# MULTIPLE CONDITIONS
# ==========================================================

number = 0

result = (
    "Positive"
    if number > 0
    else "Negative"
    if number < 0
    else "Zero"
)

print(result)

# Output:

# Zero

# This is called a nested conditional expression.


# ==========================================================
# SHORT-HAND IF WITHOUT ELSE
# ==========================================================

# A normal short-hand if can also be written.

age = 20

if age >= 18:
    print("Adult")


# This can be written in one line:

if age >= 18: print("Adult")

# Output:

# Adult


# ==========================================================
# SHORT-HAND IF-ELSE WITH PRINT
# ==========================================================

age = 16

print("Adult" if age >= 18 else "Minor")

# Output:

# Minor


# ==========================================================
# SHORT-HAND IF-ELSE WITH INPUT
# ==========================================================

number = int(input("Enter a number: "))

result = "Even" if number % 2 == 0 else "Odd"

print(result)


# ==========================================================
# SHORT-HAND IF-ELSE WITH STRING
# ==========================================================

name = "Bhalbheem"

message = "Name exists" if name else "Name is empty"

print(message)

# Output:

# Name exists


# ==========================================================
# WHY USE SHORT-HAND IF-ELSE?
# ==========================================================

'''It is useful when the condition is simple and
the result is short.

It makes simple conditional assignments more concise.'''


# ==========================================================
# WHEN NOT TO USE IT
# ==========================================================

'''Avoid using complicated nested conditional expressions
because they can make the code difficult to read.

For complex conditions, normal if-else statements
are usually clearer.'''


# ==========================================================
# NORMAL IF-ELSE VS SHORT-HAND IF-ELSE
# ==========================================================

# Normal:

if age >= 18:

    status = "Adult"

else:

    status = "Minor"


# Short-hand:

status = "Adult" if age >= 18 else "Minor"


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# • Short-hand if-else is also called a conditional expression.
# • It allows a simple if-else to be written in one line.
# • It returns one value based on a condition.
# • It can be used for assigning variables.
# • It can be used directly inside print().
# • Complex nested expressions should generally be avoided.


# ==========================================================
# QUICK REVISION
# ==========================================================

# Syntax:

# value_if_true if condition else value_if_false


# Example:

result = "Even" if number % 2 == 0 else "Odd"


# ==========================================================
# SUMMARY
# ==========================================================

# • Short-hand if-else provides a concise way to write if-else.
# • It is useful for simple conditions.
# • It can be used directly in assignments.
# • It can also be used inside expressions.
# • Normal if-else is better for complex logic.
