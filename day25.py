# ==========================================================
# PYTHON DAY 25
# DICTIONARIES
# ==========================================================


# ==========================================================
# WHAT IS A DICTIONARY?
# ==========================================================

# A dictionary is a collection of data stored
# in key-value pairs.

# Dictionary is created using curly brackets {}.

student = {
    "name": "Bhalbheem",
    "age": 17,
    "branch": "CSE"
}

print(student)

# Output:

# {'name': 'Bhalbheem', 'age': 17, 'branch': 'CSE'}


# ==========================================================
# KEY-VALUE PAIR
# ==========================================================

# Every item in a dictionary has:

# Key   → identifies the data
# Value → actual data

student = {
    "name": "Bhalbheem",
    "age": 17
}

# "name" → key
# "Bhalbheem" → value
#
# "age" → key
# 17 → value


# ==========================================================
# ACCESSING VALUES
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17,
    "branch": "CSE"
}

print(student["name"])
print(student["age"])
print(student["branch"])

# Output:

# Bhalbheem
# 17
# CSE


# ==========================================================
# ACCESSING A NON-EXISTING KEY
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17
}

# print(student["branch"])

# This raises a KeyError because
# "branch" does not exist in the dictionary.


# ==========================================================
# ADDING A NEW KEY-VALUE PAIR
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17
}

student["branch"] = "CSE"

print(student)

# Output:

# {'name': 'Bhalbheem', 'age': 17, 'branch': 'CSE'}


# ==========================================================
# UPDATING A VALUE
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17
}

student["age"] = 18

print(student)

# Output:

# {'name': 'Bhalbheem', 'age': 18}


# ==========================================================
# DICTIONARY IS MUTABLE
# ==========================================================

# Dictionaries are mutable.

# This means their contents can be changed
# after the dictionary is created.

student = {
    "name": "Bhalbheem",
    "age": 17
}

student["age"] = 18
student["branch"] = "CSE"

print(student)


# ==========================================================
# DUPLICATE KEYS
# ==========================================================

# Dictionary keys must be unique.

student = {
    "name": "Bhalbheem",
    "age": 17,
    "age": 18
}

print(student)

# Output:

# {'name': 'Bhalbheem', 'age': 18}

# If the same key is written more than once,
# the last value is used.


# ==========================================================
# DUPLICATE VALUES
# ==========================================================

# Values can be duplicated.

student = {
    "name": "Bhalbheem",
    "father_name": "Bhalbheem",
    "city": "Hyderabad"
}

print(student)

# Duplicate values are allowed.


# ==========================================================
# DIFFERENT DATA TYPES
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17,
    "marks": 95.5,
    "passed": True
}

print(student)

# Keys and values can contain different data types,
# depending on whether they are valid dictionary keys/values.


# ==========================================================
# LIST AS A VALUE
# ==========================================================

student = {
    "name": "Bhalbheem",
    "marks": [90, 85, 95]
}

print(student["marks"])

# Output:

# [90, 85, 95]

# A dictionary value can be a list.


# ==========================================================
# DICTIONARY AS A VALUE
# ==========================================================

student = {
    "name": "Bhalbheem",
    "details": {
        "age": 17,
        "branch": "CSE"
    }
}

print(student)

# A dictionary can contain another dictionary
# as a value.


# ==========================================================
# NESTED DICTIONARY
# ==========================================================

students = {
    "student1": {
        "name": "Alice",
        "age": 18
    },
    "student2": {
        "name": "Bob",
        "age": 19
    }
}

print(students)

# This is called a nested dictionary.


# ==========================================================
# ACCESSING NESTED DICTIONARY
# ==========================================================

students = {
    "student1": {
        "name": "Alice",
        "age": 18
    }
}

print(students["student1"]["name"])
print(students["student1"]["age"])

# Output:

# Alice
# 18


# ==========================================================
# DICTIONARY LENGTH
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17,
    "branch": "CSE"
}

print(len(student))

# Output:

# 3

# len() returns the number of key-value pairs.


# ==========================================================
# CHECKING WHETHER A KEY EXISTS
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17
}

print("name" in student)
print("branch" in student)

# Output:

# True
# False

# The 'in' operator checks dictionary keys.


# ==========================================================
# NOT IN
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17
}

print("branch" not in student)

# Output:

# True


# ==========================================================
# LOOPING THROUGH A DICTIONARY
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17,
    "branch": "CSE"
}

for key in student:
    print(key)

# Output:

# name
# age
# branch

# By default, looping through a dictionary
# gives its keys.


# ==========================================================
# DICTIONARY WITH NUMERIC KEYS
# ==========================================================

marks = {
    1: 90,
    2: 85,
    3: 95
}

print(marks[1])

# Output:

# 90


# ==========================================================
# DIFFERENT KEY TYPES
# ==========================================================

data = {
    "name": "Python",
    1: "One",
    2.5: "Decimal"
}

print(data["name"])
print(data[1])
print(data[2.5])


# ==========================================================
# IMPORTANT: DICTIONARY KEYS
# ==========================================================

# Dictionary keys must be hashable.

# Common valid keys:

data = {
    "name": "Python",
    1: "One",
    2.5: "Two Point Five",
    (1, 2): "Tuple"
}

# Lists cannot be used as dictionary keys.

# Example:

# data = {
#     [1, 2]: "List"
# }

# This raises a TypeError.


# ==========================================================
# DICTIONARY VS LIST
# ==========================================================

# List:

students = ["Alice", "Bob", "Charlie"]

# Data is accessed using indexes.

print(students[0])

# Dictionary:

students = {
    "first": "Alice",
    "second": "Bob",
    "third": "Charlie"
}

# Data is accessed using keys.

print(students["first"])


# ==========================================================
# DICTIONARY VS TUPLE
# ==========================================================

# Tuple:

student = ("Bhalbheem", 17, "CSE")

# Access using indexes.

print(student[0])


# Dictionary:

student = {
    "name": "Bhalbheem",
    "age": 17,
    "branch": "CSE"
}

# Access using meaningful keys.

print(student["name"])


# ==========================================================
# DICTIONARY VS SET
# ==========================================================

# Set:

numbers = {10, 20, 30}

# Contains individual unique values.


# Dictionary:

numbers = {
    "first": 10,
    "second": 20,
    "third": 30
}

# Contains key-value pairs.


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# Dictionary stores data as key-value pairs.

# Dictionaries are created using {}.

# Keys are used to access values.

# Dictionary keys must be unique.

# Duplicate values are allowed.

# Dictionaries are mutable.

# Dictionaries can contain different data types.

# Dictionaries can contain lists, tuples,
# sets, and other dictionaries as values.

# Nested dictionaries are dictionaries
# inside other dictionaries.

# len() returns the number of key-value pairs.

# 'in' checks whether a key exists.

# ==========================================================
# QUICK REVISION
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17,
    "branch": "CSE"
}

# Access value
print(student["name"])

# Add new key-value pair
student["college"] = "KMIT"

# Update value
student["age"] = 18

print(student)
