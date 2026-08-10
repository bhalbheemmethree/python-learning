# ==========================================================
# PYTHON DAY 18
# TUPLES
# ==========================================================


# ==========================================================
# WHAT IS A TUPLE?
# ==========================================================

# A tuple is a collection of multiple values
# stored in a single variable.

# Tuples are ordered and immutable.

# Tuples are created using parentheses ().


# ==========================================================
# CREATING A TUPLE
# ==========================================================

numbers = (10, 20, 30, 40, 50)

print(numbers)

# Output

# (10, 20, 30, 40, 50)


# ==========================================================
# TUPLE WITH DIFFERENT DATA TYPES
# ==========================================================

data = (10, "Python", 3.14, True)

print(data)

# Output

# (10, 'Python', 3.14, True)

# A tuple can contain different data types.


# ==========================================================
# ACCESSING TUPLE ELEMENTS
# ==========================================================

numbers = (10, 20, 30, 40, 50)

print(numbers[0])
print(numbers[2])
print(numbers[4])

# Output

# 10
# 30
# 50

# Tuple indexing starts from 0.


# ==========================================================
# POSITIVE INDEXING
# ==========================================================

numbers = (10, 20, 30, 40, 50)

# Index:
#  0   1   2   3   4

print(numbers[0])  # 10
print(numbers[1])  # 20
print(numbers[2])  # 30
print(numbers[3])  # 40
print(numbers[4])  # 50


# ==========================================================
# NEGATIVE INDEXING
# ==========================================================

numbers = (10, 20, 30, 40, 50)

print(numbers[-1])
print(numbers[-2])
print(numbers[-5])

# Output

# 50
# 40
# 10

# Negative indexing starts from the end.

# -1 -> Last element
# -2 -> Second-last element


# ==========================================================
# TUPLE IS IMMUTABLE
# ==========================================================

numbers = (10, 20, 30)

# numbers[0] = 100

# This raises a TypeError.

# Tuples cannot be changed after they are created.

# You cannot directly:
# - Change an element
# - Add an element
# - Remove an element


# ==========================================================
# LIST VS TUPLE
# ==========================================================

numbers_list = [10, 20, 30]

numbers_tuple = (10, 20, 30)

# List -> Mutable
# Tuple -> Immutable

# List uses []
# Tuple uses ()

# Both are ordered collections
# and support indexing.


# ==========================================================
# TUPLE WITH DUPLICATE VALUES
# ==========================================================

numbers = (10, 20, 10, 30, 20)

print(numbers)

# Output

# (10, 20, 10, 30, 20)

# Duplicate values are allowed.


# ==========================================================
# EMPTY TUPLE
# ==========================================================

numbers = ()

print(numbers)

# Output

# ()


# ==========================================================
# SINGLE-ELEMENT TUPLE
# ==========================================================

number = (10,)

print(number)

# Output

# (10,)

# A comma is required to create a
# single-element tuple.

# Without the comma:

number = (10)

print(type(number))

# Output

# <class 'int'>

# (10) is an integer, not a tuple.


# ==========================================================
# MIXED DATA IN TUPLE
# ==========================================================

student = ("Bhalbheem", 17, 85.5, True)

print(student[0])
print(student[1])
print(student[2])
print(student[3])

# Output

# Bhalbheem
# 17
# 85.5
# True


# ==========================================================
# NESTED TUPLE
# ==========================================================

numbers = ((1, 2), (3, 4), (5, 6))

print(numbers)

# Output

# ((1, 2), (3, 4), (5, 6))

# A tuple inside another tuple
# is called a nested tuple.


# ==========================================================
# ACCESSING NESTED TUPLE
# ==========================================================

numbers = ((1, 2), (3, 4), (5, 6))

print(numbers[0])
print(numbers[1][0])
print(numbers[2][1])

# Output

# (1, 2)
# 3
# 6


# ==========================================================
# TUPLES ARE ORDERED
# ==========================================================

numbers = (30, 10, 20)

print(numbers)

# Output

# (30, 10, 20)

# The order of elements is maintained.


# ==========================================================
# TUPLES CAN CONTAIN OTHER COLLECTIONS
# ==========================================================

data = ([1, 2, 3], "Python")

print(data)

# Output

# ([1, 2, 3], 'Python')

# A tuple can contain a list or other objects.


# ==========================================================
# IMPORTANT POINT
# ==========================================================

# The tuple itself is immutable.

data = ([1, 2, 3], "Python")

data[0].append(4)

print(data)

# Output

# ([1, 2, 3, 4], 'Python')

# The tuple still cannot have its elements replaced,
# but a mutable object inside it can sometimes be modified.


# ==========================================================
# CHECKING TYPE
# ==========================================================

numbers = (10, 20, 30)

print(type(numbers))

# Output

# <class 'tuple'>


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# Tuples are created using ().

# Tuples are ordered.

# Tuples are immutable.

# Tuples support indexing.

# Positive indexing starts from 0.

# Negative indexing starts from -1.

# Tuples can contain different data types.

# Duplicate values are allowed.

# Tuples can contain nested tuples.

# A single-element tuple requires a comma.

# Tuples are different from lists because
# lists are mutable while tuples are immutable.


# ==========================================================
# IMPORTANT
# ==========================================================

# Tuple operations are NOT covered today.

# Concatenation
# Repetition
# Membership
# len()
# Slicing
# count()
# index()
# Tuple unpacking
