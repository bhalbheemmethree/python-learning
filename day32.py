# ==========================================================
# PYTHON DAY 32
# ENUMERATE() FUNCTION
# ==========================================================


# ==========================================================
# WHAT IS enumerate()?
# ==========================================================

Definition:

The enumerate() function is used to loop through a sequence
while getting both the index and the value at the same time.

It is commonly used with:

• Lists
• Tuples
• Strings
• Other iterable objects


# ==========================================================
# BASIC SYNTAX
# ==========================================================

enumerate(iterable, start=0)


# start is optional.

# By default, indexing starts from 0.


# ==========================================================
# BASIC EXAMPLE
# ==========================================================

names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):

    print(index, name)

# Output:

# 0 Alice
# 1 Bob
# 2 Charlie


# ==========================================================
# WHY USE enumerate()?
# ==========================================================

Without enumerate(), we may need to manually maintain
an index.

Example:

names = ["Alice", "Bob", "Charlie"]

for i in range(len(names)):

    print(i, names[i])


# enumerate() makes this simpler:

for i, name in enumerate(names):

    print(i, name)


# ==========================================================
# ENUMERATE() WITH STARTING INDEX
# ==========================================================

names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names, start=1):

    print(index, name)

# Output:

# 1 Alice
# 2 Bob
# 3 Charlie


# ==========================================================
# STARTING INDEX FROM 10
# ==========================================================

names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names, start=10):

    print(index, name)

# Output:

# 10 Alice
# 11 Bob
# 12 Charlie


# ==========================================================
# ENUMERATE() WITH LIST
# ==========================================================

fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):

    print("Index:", index)
    print("Fruit:", fruit)


# ==========================================================
# ENUMERATE() WITH STRING
# ==========================================================

word = "Python"

for index, character in enumerate(word):

    print(index, character)

# Output:

# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n


# ==========================================================
# ENUMERATE() WITH TUPLE
# ==========================================================

numbers = (10, 20, 30, 40)

for index, number in enumerate(numbers):

    print(index, number)

# Output:

# 0 10
# 1 20
# 2 30
# 3 40


# ==========================================================
# ENUMERATE() WITH CONDITIONS
# ==========================================================

names = ["Alice", "Bob", "Charlie", "David"]

for index, name in enumerate(names):

    if name == "Charlie":

        print("Found at index:", index)

# Output:

# Found at index: 2


# ==========================================================
# ENUMERATE() WITH IF-ELSE
# ==========================================================

marks = [80, 45, 90, 30]

for index, mark in enumerate(marks):

    if mark >= 50:

        print(index, "Pass")

    else:

        print(index, "Fail")

# Output:

# 0 Pass
# 1 Fail
# 2 Pass
# 3 Fail


# ==========================================================
# ENUMERATE() WITH START=1
# ==========================================================

subjects = ["Python", "Java", "SQL"]

for number, subject in enumerate(subjects, start=1):

    print(number, subject)

# Output:

# 1 Python
# 2 Java
# 3 SQL


# ==========================================================
# ENUMERATE() VS range(len())
# ==========================================================

# Without enumerate():

names = ["Alice", "Bob", "Charlie"]

for i in range(len(names)):

    print(i, names[i])


# With enumerate():

for i, name in enumerate(names):

    print(i, name)


# enumerate() is generally cleaner when you need
# both the index and the value.


# ==========================================================
# CONVERT enumerate() TO A LIST
# ==========================================================

names = ["Alice", "Bob", "Charlie"]

result = list(enumerate(names))

print(result)

# Output:

# [(0, 'Alice'), (1, 'Bob'), (2, 'Charlie')]


# ==========================================================
# ENUMERATE() RETURNS PAIRS
# ==========================================================

names = ["Alice", "Bob"]

for item in enumerate(names):

    print(item)

# Output:

# (0, 'Alice')
# (1, 'Bob')


# Each item contains:

# index + value


# ==========================================================
# UNPACKING enumerate()
# ==========================================================

names = ["Alice", "Bob"]

for index, name in enumerate(names):

    print(index)
    print(name)

# Python automatically unpacks each pair into:

# index
# name


# ==========================================================
# ENUMERATE() WITH NESTED LIST
# ==========================================================

students = [
    ["Alice", 90],
    ["Bob", 80],
    ["Charlie", 85]
]

for index, student in enumerate(students):

    print(index, student)

# Output:

# 0 ['Alice', 90]
# 1 ['Bob', 80]
# 2 ['Charlie', 85]


# ==========================================================
# ENUMERATE() WITH BREAK
# ==========================================================

names = ["Alice", "Bob", "Charlie", "David"]

for index, name in enumerate(names):

    if name == "Charlie":

        break

    print(index, name)

# Output:

# 0 Alice
# 1 Bob


# ==========================================================
# ENUMERATE() WITH CONTINUE
# ==========================================================

names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):

    if name == "Bob":

        continue

    print(index, name)

# Output:

# 0 Alice
# 2 Charlie


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# • enumerate() provides index and value together.
# • Index starts from 0 by default.
# • The starting index can be changed using start.
# • enumerate() works with iterable objects.
# • It is commonly used inside for loops.
# • It avoids manually managing an index.
# • enumerate() returns pairs containing index and value.


# ==========================================================
# QUICK REVISION
# ==========================================================

# Syntax:

# enumerate(iterable, start=0)


# Example:

names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):

    print(index, name)


# Output:

# 0 Alice
# 1 Bob
# 2 Charlie


# ==========================================================
# SUMMARY
# ==========================================================

# • enumerate() gives both index and value while looping.
# • Default starting index is 0.
# • start can be used to change the starting index.
# • It makes indexed loops cleaner.
# • It works with lists, tuples, strings and other iterables.
# • It is commonly used with for loops.
