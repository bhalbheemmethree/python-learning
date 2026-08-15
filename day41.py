# ==========================================================
# PYTHON DAY 41
# LAMBDA FUNCTIONS
# ==========================================================


# ==========================================================
# WHAT IS A LAMBDA FUNCTION?
# ==========================================================

# Definition:

# A lambda function is a small anonymous function that
# can contain a single expression.

# Anonymous means it does not require a normal function name.

# Syntax:

# lambda arguments: expression


# ==========================================================
# BASIC EXAMPLE
# ==========================================================

square = lambda x: x * x

print(square(5))

# Output:

# 25


# ==========================================================
# NORMAL FUNCTION VS LAMBDA
# ==========================================================

# Normal function:

def square(x):

    return x * x


print(square(5))


# Lambda function:

square = lambda x: x * x

print(square(5))


# Both produce:

# 25


# ==========================================================
# LAMBDA WITH TWO ARGUMENTS
# ==========================================================

add = lambda a, b: a + b

print(add(10, 20))

# Output:

# 30


# ==========================================================
# LAMBDA WITH THREE ARGUMENTS
# ==========================================================

multiply = lambda a, b, c: a * b * c

print(multiply(2, 3, 4))

# Output:

# 24


# ==========================================================
# LAMBDA FUNCTION WITH NO ARGUMENTS
# ==========================================================

greet = lambda: "Hello Python"

print(greet())

# Output:

# Hello Python


# ==========================================================
# LAMBDA WITH CONDITIONAL EXPRESSION
# ==========================================================

check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))

# Output:

# Even


# ==========================================================
# LAMBDA FUNCTION IS AN EXPRESSION
# ==========================================================

# Example:

square = lambda x: x ** 2

# The expression:

# x ** 2

# is evaluated and returned automatically.


# ==========================================================
# RETURN IS NOT USED
# ==========================================================

# Normal function:

def square(x):

    return x * x


# Lambda:

square = lambda x: x * x


# A lambda function automatically returns
# the result of its expression.


# ==========================================================
# LAMBDA CAN BE STORED IN A VARIABLE
# ==========================================================

double = lambda x: x * 2

print(double(10))

# Output:

# 20


# ==========================================================
# LAMBDA WITH STRING
# ==========================================================

length = lambda text: len(text)

print(length("Python"))

# Output:

# 6


# ==========================================================
# LAMBDA WITH max()
# ==========================================================

numbers = [10, 25, 5, 40, 15]

result = max(numbers, key=lambda x: x)

print(result)

# Output:

# 40


# ==========================================================
# LAMBDA WITH min()
# ==========================================================

numbers = [10, 25, 5, 40, 15]

result = min(numbers, key=lambda x: x)

print(result)

# Output:

# 5


# ==========================================================
# LAMBDA WITH sorted()
# ==========================================================

# Definition:

# The key parameter of sorted() can use a lambda function
# to specify how items should be sorted.


numbers = [5, 2, 8, 1, 3]

result = sorted(numbers, key=lambda x: x)

print(result)

# Output:

# [1, 2, 3, 5, 8]


# ==========================================================
# SORTING STRINGS BY LENGTH
# ==========================================================

words = ["apple", "hi", "banana", "cat"]

result = sorted(words, key=lambda word: len(word))

print(result)

# Output:

# ['hi', 'cat', 'apple', 'banana']


# ==========================================================
# LAMBDA WITH LIST OF TUPLES
# ==========================================================

students = [
    ("Alice", 85),
    ("Bob", 70),
    ("Charlie", 95)
]

result = sorted(students, key=lambda student: student[1])

print(result)

# Output:

# [('Bob', 70), ('Alice', 85), ('Charlie', 95)]


# ==========================================================
# LAMBDA WITH dictionary
# ==========================================================

students = {
    "Alice": 85,
    "Bob": 70,
    "Charlie": 95
}

result = sorted(
    students.items(),
    key=lambda item: item[1]
)

print(result)

# Output:

# [('Bob', 70), ('Alice', 85), ('Charlie', 95)]


# ==========================================================
# LAMBDA WITH map()
# ==========================================================

# Lambda functions are commonly used with map().

# Example:

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)

# Output:

# [1, 4, 9, 16, 25]


# map(), filter() and reduce() will be covered
# in detail in Day 42.


# ==========================================================
# LAMBDA WITH filter()
# ==========================================================

numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

# Output:

# [2, 4, 6]


# Detailed map(), filter() and reduce()
# will be covered in Day 42.


# ==========================================================
# IMPORTANT RULES OF LAMBDA
# ==========================================================

# A lambda function:

# • Uses the lambda keyword.
# • Can accept multiple arguments.
# • Contains a single expression.
# • Automatically returns the expression's result.
# • Does not use a normal return statement.
# • Is commonly used for short operations.


# ==========================================================
# LAMBDA LIMITATION
# ==========================================================

# Lambda functions are designed for simple expressions.

# Example:

square = lambda x: x * x


# For complicated logic, a normal def function
# is usually clearer.


# ==========================================================
# LAMBDA VS def
# ==========================================================

# Lambda:

square = lambda x: x * x


# Normal function:

def square(x):

    return x * x


# Lambda is shorter.

# Normal functions are generally better for
# larger or more complicated logic.


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# • Lambda creates a small anonymous function.
# • Syntax is lambda arguments: expression.
# • It can take multiple arguments.
# • It contains one expression.
# • The expression's result is automatically returned.
# • Lambda functions are useful for short operations.
# • They are commonly used with functions such as
#   sorted(), map() and filter().
# • Normal def functions are better for complex logic.


# ==========================================================
# QUICK REVISION
# ==========================================================

# One argument:

square = lambda x: x * x


# Two arguments:

add = lambda a, b: a + b


# Conditional:

check = lambda x: "Even" if x % 2 == 0 else "Odd"


# With sorted():

words = ["apple", "hi", "banana"]

words.sort(key=lambda word: len(word))


# ==========================================================
# SUMMARY
# ==========================================================

# • Lambda functions are small anonymous functions.
# • They use the lambda keyword.
# • They can accept arguments.
# • They contain a single expression.
# • The expression result is returned automatically.
# • They are useful when a small function is needed temporarily.
# • They are commonly used with sorted(), map() and filter().
