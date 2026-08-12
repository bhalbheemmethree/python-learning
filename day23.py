# ==========================================================
# PYTHON DAY 23
# SETS
# ==========================================================


# ==========================================================
# WHAT IS A SET?
# ==========================================================

# A set is a collection of unique elements.

# Sets are:
# - Unordered
# - Mutable
# - Unindexed
# - Do not allow duplicate values

# Sets are created using curly brackets {}.


# ==========================================================
# CREATING A SET
# ==========================================================

numbers = {10, 20, 30, 40}

print(numbers)

# Output may be:

# {10, 20, 30, 40}

# The order is not guaranteed because sets are unordered.


# ==========================================================
# DUPLICATE VALUES
# ==========================================================

numbers = {10, 20, 10, 30, 20, 40}

print(numbers)

# Output:

# {10, 20, 30, 40}

# Duplicate values are automatically removed.

# A set stores only unique values.


# ==========================================================
# SET WITH DIFFERENT DATA TYPES
# ==========================================================

data = {10, "Python", 3.14, True}

print(data)

# A set can contain different data types,
# as long as the elements are valid for a set.


# ==========================================================
# SET IS UNORDERED
# ==========================================================

numbers = {30, 10, 20, 40}

print(numbers)

# You cannot rely on the order in which
# elements appear in a set.


# ==========================================================
# SET DOES NOT SUPPORT INDEXING
# ==========================================================

numbers = {10, 20, 30}

# print(numbers[0])

# This raises a TypeError.

# Sets do not have indexes because they are unordered.


# ==========================================================
# EMPTY SET
# ==========================================================

numbers = set()

print(numbers)

# Output:

# set()

# IMPORTANT:

# {} creates an empty dictionary,
# not an empty set.

empty = {}

print(type(empty))

# Output:

# <class 'dict'>


empty_set = set()

print(type(empty_set))

# Output:

# <class 'set'>


# ==========================================================
# SET WITH STRINGS
# ==========================================================

names = {"Alice", "Bob", "Charlie"}

print(names)


# ==========================================================
# SET WITH NUMBERS
# ==========================================================

marks = {80, 90, 75, 88, 95}

print(marks)


# ==========================================================
# SET WITH DUPLICATE STRINGS
# ==========================================================

languages = {"Python", "Java", "Python", "C++"}

print(languages)

# Output contains each language only once.


# ==========================================================
# SET IS MUTABLE
# ==========================================================

numbers = {10, 20, 30}

# A set itself can be changed after creation.

# Set methods used for modifying sets
# will be covered separately in Day 24.


# ==========================================================
# MEMBERSHIP OPERATOR
# ==========================================================

numbers = {10, 20, 30, 40}

print(20 in numbers)
print(50 in numbers)

# Output:

# True
# False

# 'in' checks whether an element exists in the set.


# ==========================================================
# NOT IN
# ==========================================================

numbers = {10, 20, 30, 40}

print(50 not in numbers)
print(20 not in numbers)

# Output:

# True
# False


# ==========================================================
# LENGTH OF A SET
# ==========================================================

numbers = {10, 20, 30, 40}

print(len(numbers))

# Output:

# 4

# len() returns the number of unique elements.


# ==========================================================
# SET CAN REMOVE DUPLICATES FROM A LIST
# ==========================================================

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print(unique_numbers)

# Output:

# {10, 20, 30, 40}

# Converting a list to a set removes duplicates.


# ==========================================================
# CONVERTING SET TO LIST
# ==========================================================

numbers = {10, 20, 30}

numbers_list = list(numbers)

print(numbers_list)

# The order of elements should not be relied upon.


# ==========================================================
# CONVERTING SET TO TUPLE
# ==========================================================

numbers = {10, 20, 30}

numbers_tuple = tuple(numbers)

print(numbers_tuple)

# A set can be converted into a tuple.


# ==========================================================
# NESTED COLLECTIONS
# ==========================================================

# Sets cannot contain mutable elements such as lists.

# Example:

# numbers = {[1, 2], [3, 4]}

# This raises a TypeError.


# ==========================================================
# SET VS LIST
# ==========================================================

numbers_list = [10, 20, 10, 30]

numbers_set = {10, 20, 10, 30}

print(numbers_list)
print(numbers_set)

# List:

# [10, 20, 10, 30]

# Set:

# {10, 20, 30}

# List:
# - Ordered
# - Allows duplicates
# - Supports indexing

# Set:
# - Unordered
# - Does not allow duplicates
# - Does not support indexing


# ==========================================================
# SET VS TUPLE
# ==========================================================

numbers_tuple = (10, 20, 30, 10)

numbers_set = {10, 20, 30, 10}

# Tuple:
# - Ordered
# - Allows duplicates
# - Immutable
# - Supports indexing

# Set:
# - Unordered
# - Does not allow duplicates
# - Mutable
# - Does not support indexing


# ==========================================================
# SET VS LIST VS TUPLE
# ==========================================================

# List:
# []
# Ordered
# Mutable
# Duplicates allowed
# Indexing supported


# Tuple:
# ()
# Ordered
# Immutable
# Duplicates allowed
# Indexing supported


# Set:
# {}
# Unordered
# Mutable
# Duplicates not allowed
# Indexing not supported


# ==========================================================
# ITERATING THROUGH A SET
# ==========================================================

numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)

# The elements will be printed,
# but their order is not guaranteed.


# ==========================================================
# SET WITH UNIQUE STUDENTS
# ==========================================================

students = {
    "Alice",
    "Bob",
    "Alice",
    "Charlie",
    "Bob"
}

print(students)

# Output contains:

# Alice
# Bob
# Charlie

# Duplicate names are automatically removed.


# ==========================================================
# CHECKING MEMBERSHIP
# ==========================================================

students = {"Alice", "Bob", "Charlie"}

if "Alice" in students:
    print("Alice is present")

# Output:

# Alice is present


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# Sets are created using {}.

# An empty set is created using set().

# {} creates an empty dictionary.

# Sets are unordered.

# Sets do not support indexing.

# Sets do not allow duplicate elements.

# Sets are mutable.

# Sets can contain different data types.

# len() returns the number of elements.

# in checks membership.

# not in checks non-membership.

# Sets are useful when you need unique values.
