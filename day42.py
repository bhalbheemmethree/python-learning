# ==========================================================
# PYTHON DAY 42
# map(), filter() AND reduce()
# ==========================================================


# ==========================================================
# map()
# ==========================================================

# Definition:

# map() applies a function to every item in an iterable.

# Syntax:

# map(function, iterable)


# ==========================================================
# BASIC map() EXAMPLE
# ==========================================================

numbers = [1, 2, 3, 4, 5]

squares = map(lambda x: x * x, numbers)

print(list(squares))

# Output:

# [1, 4, 9, 16, 25]


# ==========================================================
# map() WITH NORMAL FUNCTION
# ==========================================================

def square(x):

    return x * x


numbers = [1, 2, 3, 4, 5]

result = map(square, numbers)

print(list(result))

# Output:

# [1, 4, 9, 16, 25]


# ==========================================================
# map() WITH TWO LISTS
# ==========================================================

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(
    lambda x, y: x + y,
    numbers1,
    numbers2
)

print(list(result))

# Output:

# [5, 7, 9]


# ==========================================================
# IMPORTANT POINT ABOUT map()
# ==========================================================

# map() returns a map object.

# To see the results as a list:

# list(map(...))


# ==========================================================
# filter()
# ==========================================================

# Definition:

# filter() selects items from an iterable based on
# a condition.

# Syntax:

# filter(function, iterable)


# The function should return:

# True  → Keep the item
# False → Remove the item


# ==========================================================
# BASIC filter() EXAMPLE
# ==========================================================

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(
    lambda x: x % 2 == 0,
    numbers
)

print(list(even_numbers))

# Output:

# [2, 4, 6]


# ==========================================================
# filter() WITH NORMAL FUNCTION
# ==========================================================

def is_even(x):

    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]

result = filter(is_even, numbers)

print(list(result))

# Output:

# [2, 4, 6]


# ==========================================================
# FILTERING NUMBERS GREATER THAN 10
# ==========================================================

numbers = [5, 12, 8, 20, 3, 15]

result = filter(
    lambda x: x > 10,
    numbers
)

print(list(result))

# Output:

# [12, 20, 15]


# ==========================================================
# FILTERING STRINGS
# ==========================================================

words = ["apple", "hi", "banana", "cat"]

result = filter(
    lambda word: len(word) > 3,
    words
)

print(list(result))

# Output:

# ['apple', 'banana']


# ==========================================================
# reduce()
# ==========================================================

# Definition:

# reduce() repeatedly applies a function to the items
# of an iterable and reduces them to a single result.

# reduce() is available from the functools module.

# Syntax:

from functools import reduce

# reduce(function, iterable)


# ==========================================================
# BASIC reduce() EXAMPLE
# ==========================================================

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(
    lambda x, y: x + y,
    numbers
)

print(result)

# Output:

# 15


# ==========================================================
# HOW reduce() WORKS
# ==========================================================

numbers = [1, 2, 3, 4]

reduce(lambda x, y: x + y, numbers)


# Step 1:

# 1 + 2 = 3


# Step 2:

# 3 + 3 = 6


# Step 3:

# 6 + 4 = 10


# Final result:

# 10


# ==========================================================
# reduce() FOR MULTIPLICATION
# ==========================================================

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(
    lambda x, y: x * y,
    numbers
)

print(result)

# Output:

# 120


# ==========================================================
# reduce() WITH INITIAL VALUE
# ==========================================================

from functools import reduce

numbers = [1, 2, 3]

result = reduce(
    lambda x, y: x + y,
    numbers,
    10
)

print(result)

# Output:

# 16


# Calculation:

# 10 + 1 = 11
# 11 + 2 = 13
# 13 + 3 = 16


# ==========================================================
# map() VS filter() VS reduce()
# ==========================================================

# map()

# → Transforms every item.


# filter()

# → Selects items based on a condition.


# reduce()

# → Combines items into one final result.


# ==========================================================
# SIMPLE WAY TO REMEMBER
# ==========================================================

# map()
# → CHANGE


# filter()
# → SELECT


# reduce()
# → COMBINE


# ==========================================================
# COMBINING map() AND filter()
# ==========================================================

numbers = [1, 2, 3, 4, 5, 6]

result = map(
    lambda x: x * x,
    filter(lambda x: x % 2 == 0, numbers)
)

print(list(result))

# Output:

# [4, 16, 36]


# First filter:

# [2, 4, 6]


# Then map:

# [4, 16, 36]


# ==========================================================
# COMBINING filter(), map() AND reduce()
# ==========================================================

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(
    lambda x: x % 2 == 0,
    numbers
)

squares = map(
    lambda x: x * x,
    even_numbers
)

result = reduce(
    lambda x, y: x + y,
    squares
)

print(result)

# Output:

# 56


# Calculation:

# Even numbers:
# 2, 4, 6

# Squares:
# 4, 16, 36

# Sum:
# 4 + 16 + 36 = 56


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# • map() applies a function to every item.
# • filter() selects items based on a condition.
# • reduce() combines items into one result.
# • map() returns a map object.
# • filter() returns a filter object.
# • reduce() is imported from functools.
# • Lambda functions are commonly used with all three.
# • list() can be used to convert map/filter results
#   into a list.


# ==========================================================
# QUICK REVISION
# ==========================================================

# map()

# numbers = [1, 2, 3]

# result = map(lambda x: x * 2, numbers)

# print(list(result))

# [2, 4, 6]


# filter()

# numbers = [1, 2, 3, 4]

# result = filter(lambda x: x % 2 == 0, numbers)

# print(list(result))

# [2, 4]


# reduce()

# from functools import reduce

# numbers = [1, 2, 3, 4]

# result = reduce(lambda x, y: x + y, numbers)

# print(result)

# 10


# ==========================================================
# SUMMARY
# ==========================================================

# map()
# • Transforms every element.
# • Returns a map object.
# • Commonly used with lambda.

# filter()
# • Selects elements that satisfy a condition.
# • Returns a filter object.
# • Commonly used with lambda.

# reduce()
# • Reduces multiple values into one value.
# • Comes from functools.
# • Commonly used for sums, products, etc.
