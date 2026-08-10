# ==========================================================
# PYTHON DAY 22
# RECURSION
# ==========================================================


# ==========================================================
# WHAT IS RECURSION?
# ==========================================================

# Recursion is a technique where a function
# calls itself.

# A function that calls itself is called
# a recursive function.


# ==========================================================
# BASIC RECURSION
# ==========================================================

def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)


countdown(5)

# Output

# 5
# 4
# 3
# 2
# 1


# ==========================================================
# HOW RECURSION WORKS
# ==========================================================

# countdown(5)
#     ↓
# countdown(4)
#     ↓
# countdown(3)
#     ↓
# countdown(2)
#     ↓
# countdown(1)
#     ↓
# countdown(0)
#     ↓
# STOP


# ==========================================================
# BASE CASE
# ==========================================================

# The condition that stops recursion
# is called the base case.

def countdown(n):

    if n == 0:       # Base case
        return

    print(n)

    countdown(n - 1)


# Without a base case, the function
# would continue calling itself.


# ==========================================================
# RECURSIVE CASE
# ==========================================================

# The part where the function calls itself
# is called the recursive case.

def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)     # Recursive case


# ==========================================================
# BASIC RECURSION EXAMPLE
# ==========================================================

def print_numbers(n):

    if n == 0:
        return

    print(n)

    print_numbers(n - 1)


print_numbers(3)

# Output

# 3
# 2
# 1


# ==========================================================
# RECURSION WITH INCREASING VALUES
# ==========================================================

def count(n):

    if n > 5:
        return

    print(n)

    count(n + 1)


count(1)

# Output

# 1
# 2
# 3
# 4
# 5


# ==========================================================
# SUM OF NUMBERS USING RECURSION
# ==========================================================

def sum_numbers(n):

    if n == 0:
        return 0

    return n + sum_numbers(n - 1)


result = sum_numbers(5)

print(result)

# Output

# 15

# Calculation:

# 5 + 4 + 3 + 2 + 1
# = 15


# ==========================================================
# HOW sum_numbers() WORKS
# ==========================================================

# sum_numbers(5)
# = 5 + sum_numbers(4)
#
# = 5 + 4 + sum_numbers(3)
#
# = 5 + 4 + 3 + sum_numbers(2)
#
# = 5 + 4 + 3 + 2 + sum_numbers(1)
#
# = 5 + 4 + 3 + 2 + 1 + sum_numbers(0)
#
# sum_numbers(0) = 0
#
# Result = 15


# ==========================================================
# FACTORIAL USING RECURSION
# ==========================================================

# Factorial of n:
#
# n! = n × (n-1) × (n-2) ... × 1

def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))

# Output

# 120


# ==========================================================
# FACTORIAL CALCULATION
# ==========================================================

# factorial(5)
# = 5 × factorial(4)
#
# = 5 × 4 × factorial(3)
#
# = 5 × 4 × 3 × factorial(2)
#
# = 5 × 4 × 3 × 2 × factorial(1)
#
# = 5 × 4 × 3 × 2 × 1 × factorial(0)
#
# factorial(0) = 1
#
# Result = 120


# ==========================================================
# RECURSION WITH A STRING
# ==========================================================

def print_string(text, n):

    if n == 0:
        return

    print(text)

    print_string(text, n - 1)


print_string("Python", 3)

# Output

# Python
# Python
# Python


# ==========================================================
# RECURSION WITH A LIST
# ==========================================================

def print_list(numbers, index):

    if index == len(numbers):
        return

    print(numbers[index])

    print_list(numbers, index + 1)


numbers = [10, 20, 30, 40]

print_list(numbers, 0)

# Output

# 10
# 20
# 30
# 40


# ==========================================================
# RECURSION MUST MOVE TOWARDS THE BASE CASE
# ==========================================================

def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)


# Here n decreases by 1,
# so eventually n becomes 0.


# ==========================================================
# INFINITE RECURSION
# ==========================================================

# Example of BAD recursion:

# def test(n):
#     print(n)
#     test(n)

# test(5)

# The function never reaches a stopping condition.

# Python eventually raises:

# RecursionError


# ==========================================================
# RECURSION VS LOOP
# ==========================================================

# Loop:

for i in range(1, 6):
    print(i)


# Recursion:

def print_numbers(n):

    if n == 0:
        return

    print_numbers(n - 1)
    print(n)

print_numbers(5)


# Both can solve many of the same problems,
# but recursion solves a problem by
# repeatedly calling a function.


# ==========================================================
# IMPORTANT PARTS OF RECURSION
# ==========================================================

# 1. Base case
#    -> Stops the recursion.

# 2. Recursive case
#    -> Function calls itself.

# 3. Progress toward base case
#    -> Each call must move closer to stopping.


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# Recursion means a function calls itself.

# A recursive function must have a base case.

# The base case stops recursion.

# The recursive case calls the function again.

# Each recursive call should move toward
# the base case.

# Without a proper stopping condition,
# recursion can become infinite.

# Python limits recursion depth.


# ==========================================================
# QUICK REVISION
# ==========================================================

def factorial(n):

    if n == 0:              # Base case
        return 1

    return n * factorial(n - 1)  # Recursive case


print(factorial(5))

# Output

# 120
