# ==========================================================
# PYTHON DAY 16
# LISTS
# ==========================================================


# ==========================================================
# WHAT IS A LIST?
# ==========================================================

# A list is a collection of multiple values stored
# in a single variable.

# Lists are ordered and mutable.

# Lists are created using square brackets [].


# ==========================================================
# CREATING A LIST
# ==========================================================

numbers = [10, 20, 30, 40, 50]

print(numbers)

# Output

# [10, 20, 30, 40, 50]


# ==========================================================
# LIST WITH DIFFERENT DATA TYPES
# ==========================================================

data = [10, "Python", 3.14, True]

print(data)

# Output

# [10, 'Python', 3.14, True]

# A list can contain different data types.


# ==========================================================
# ACCESSING LIST ELEMENTS
# ==========================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
print(numbers[4])

# Output

# 10
# 30
# 50

# List indexing starts from 0.


# ==========================================================
# POSITIVE INDEXING
# ==========================================================

numbers = [10, 20, 30, 40, 50]

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

numbers = [10, 20, 30, 40, 50]

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
# -3 -> Third-last element


# ==========================================================
# CHANGING LIST ELEMENTS
# ==========================================================

numbers = [10, 20, 30, 40]

numbers[1] = 100

print(numbers)

# Output

# [10, 100, 30, 40]

# Lists are mutable.
# This means their elements can be changed.


# ==========================================================
# CHANGING MULTIPLE ELEMENTS
# ==========================================================

numbers = [10, 20, 30, 40, 50]

numbers[1] = 200
numbers[3] = 400

print(numbers)

# Output

# [10, 200, 30, 400, 50]


# ==========================================================
# LIST CAN CONTAIN DUPLICATE VALUES
# ==========================================================

numbers = [10, 20, 10, 30, 20]

print(numbers)

# Output

# [10, 20, 10, 30, 20]

# Duplicate values are allowed in lists.


# ==========================================================
# EMPTY LIST
# ==========================================================

numbers = []

print(numbers)

# Output

# []

# An empty list contains no elements.


# ==========================================================
# LIST WITH STRINGS
# ==========================================================

names = ["Alice", "Bob", "Charlie", "David"]

print(names[0])
print(names[2])

# Output

# Alice
# Charlie


# ==========================================================
# LIST WITH NUMBERS
# ==========================================================

marks = [85, 90, 76, 92, 88]

print(marks[0])

# Output

# 85


# ==========================================================
# LIST LENGTH
# ==========================================================

numbers = [10, 20, 30, 40, 50]

print(len(numbers))

# Output

# 5

# len() returns the number of elements in a list.


# ==========================================================
# CHECKING MEMBERSHIP
# ==========================================================

numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)

# Output

# True
# False

# 'in' checks whether a value exists in the list.


# ==========================================================
# NOT IN
# ==========================================================

numbers = [10, 20, 30, 40]

print(50 not in numbers)
print(20 not in numbers)

# Output

# True
# False


# ==========================================================
# CONCATENATING LISTS
# ==========================================================

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)

# Output

# [1, 2, 3, 4, 5, 6]

# + combines two lists into a new list.


# ==========================================================
# REPEATING A LIST
# ==========================================================

numbers = [1, 2, 3]

result = numbers * 3

print(result)

# Output

# [1, 2, 3, 1, 2, 3, 1, 2, 3]

# * repeats the elements of a list.


# ==========================================================
# NESTED LIST
# ==========================================================

numbers = [[1, 2], [3, 4], [5, 6]]

print(numbers)

# Output

# [[1, 2], [3, 4], [5, 6]]

# A list inside another list is called a nested list.


# ==========================================================
# ACCESSING NESTED LIST ELEMENTS
# ==========================================================

numbers = [[1, 2], [3, 4], [5, 6]]

print(numbers[0])
print(numbers[1][0])
print(numbers[2][1])

# Output

# [1, 2]
# 3
# 6


# ==========================================================
# LIST WITH MIXED DATA
# ==========================================================

student = ["Bhalbheem", 17, 85.5, True]

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
# LISTS ARE ORDERED
# ==========================================================

numbers = [30, 10, 20]

print(numbers)

# Output

# [30, 10, 20]

# The order in which elements are stored is maintained.


# ==========================================================
# LIST VS STRING
# ==========================================================

# String:

name = "Python"

# List:

languages = ["Python", "Java", "C++"]

# A string stores characters as a sequence.
# A list can store multiple values and different data types.
