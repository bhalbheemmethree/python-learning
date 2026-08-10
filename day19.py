# ==========================================================
# PYTHON DAY 19
# OPERATIONS ON TUPLES
# ==========================================================


# ==========================================================
# CONCATENATION (+)
# ==========================================================

# + is used to combine two tuples.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)

# Output

# (1, 2, 3, 4, 5, 6)


# ==========================================================
# REPETITION (*)
# ==========================================================

# * repeats the elements of a tuple.

numbers = (1, 2, 3)

result = numbers * 3

print(result)

# Output

# (1, 2, 3, 1, 2, 3, 1, 2, 3)


# ==========================================================
# MEMBERSHIP OPERATOR (in)
# ==========================================================

# in checks whether a value exists in a tuple.

numbers = (10, 20, 30, 40)

print(20 in numbers)
print(50 in numbers)

# Output

# True
# False


# ==========================================================
# MEMBERSHIP OPERATOR (not in)
# ==========================================================

numbers = (10, 20, 30, 40)

print(50 not in numbers)
print(20 not in numbers)

# Output

# True
# False


# ==========================================================
# len()
# ==========================================================

# len() returns the number of elements in a tuple.

numbers = (10, 20, 30, 40, 50)

print(len(numbers))

# Output

# 5


# ==========================================================
# INDEXING
# ==========================================================

# Indexing is used to access individual elements.

numbers = (10, 20, 30, 40)

print(numbers[0])
print(numbers[2])

# Output

# 10
# 30


# ==========================================================
# NEGATIVE INDEXING
# ==========================================================

numbers = (10, 20, 30, 40)

print(numbers[-1])
print(numbers[-2])

# Output

# 40
# 30


# ==========================================================
# SLICING
# ==========================================================

# Slicing is used to extract a part of a tuple.

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

# Output

# (20, 30, 40)

# Syntax:

# tuple[start:stop]

# start is included.
# stop is not included.


# ==========================================================
# SLICING FROM THE BEGINNING
# ==========================================================

numbers = (10, 20, 30, 40, 50)

print(numbers[:3])

# Output

# (10, 20, 30)


# ==========================================================
# SLICING TO THE END
# ==========================================================

numbers = (10, 20, 30, 40, 50)

print(numbers[2:])

# Output

# (30, 40, 50)


# ==========================================================
# SLICING WITH STEP
# ==========================================================

numbers = (10, 20, 30, 40, 50)

print(numbers[::2])

# Output

# (10, 30, 50)

# The step decides how many positions
# to move at a time.


# ==========================================================
# REVERSE A TUPLE USING SLICING
# ==========================================================

numbers = (10, 20, 30, 40, 50)

print(numbers[::-1])

# Output

# (50, 40, 30, 20, 10)


# ==========================================================
# count()
# ==========================================================

# count() returns how many times
# a value appears in a tuple.

numbers = (10, 20, 20, 30, 20)

print(numbers.count(20))

# Output

# 3


# ==========================================================
# index()
# ==========================================================

# index() returns the index of the first occurrence
# of a specified value.

numbers = (10, 20, 30, 20)

print(numbers.index(20))

# Output

# 1

# The first 20 is at index 1.


# ==========================================================
# ITERATING THROUGH A TUPLE
# ==========================================================

numbers = (10, 20, 30, 40)

for number in numbers:
    print(number)

# Output

# 10
# 20
# 30
# 40


# ==========================================================
# TUPLE UNPACKING
# ==========================================================

# Tuple unpacking assigns tuple values
# to separate variables.

numbers = (10, 20, 30)

a, b, c = numbers

print(a)
print(b)
print(c)

# Output

# 10
# 20
# 30


# ==========================================================
# TUPLE UNPACKING WITH DIFFERENT DATA
# ==========================================================

student = ("Bhalbheem", 17, "CSE")

name, age, branch = student

print(name)
print(age)
print(branch)

# Output

# Bhalbheem
# 17
# CSE


# ==========================================================
# SWAPPING VALUES USING TUPLE UNPACKING
# ==========================================================

a = 10
b = 20

a, b = b, a

print(a)
print(b)

# Output

# 20
# 10

# Python uses tuple unpacking to swap the values.


# ==========================================================
# IMMUTABILITY DURING OPERATIONS
# ==========================================================

numbers = (10, 20, 30)

# numbers[0] = 100

# This raises a TypeError.

# Tuple elements cannot be changed directly.


# ==========================================================
# CONCATENATION CREATES A NEW TUPLE
# ==========================================================

tuple1 = (1, 2)
tuple2 = (3, 4)

result = tuple1 + tuple2

print(tuple1)
print(tuple2)
print(result)

# Output

# (1, 2)
# (3, 4)
# (1, 2, 3, 4)

# The original tuples are not changed.


# ==========================================================
# IMPORTANT DIFFERENCES
# ==========================================================

# +       -> Combines tuples.

# *       -> Repeats a tuple.

# in      -> Checks whether a value exists.

# not in  -> Checks whether a value does not exist.

# len()   -> Returns number of elements.

# []      -> Used for indexing.

# [start:stop] -> Used for slicing.

# count() -> Counts occurrences.

# index() -> Finds the first index of a value.

# for     -> Can be used to iterate through a tuple.

# unpacking -> Assigns tuple elements to variables.


# ==========================================================
# QUICK REVISION
# ==========================================================

numbers = (10, 20, 30, 40, 50)

print(numbers[0])       # Indexing
print(numbers[-1])      # Negative indexing
print(numbers[1:4])     # Slicing
print(len(numbers))     # Length
print(30 in numbers)    # Membership
print(numbers.count(20))
print(numbers.index(30))


# ==========================================================
# IMPORTANT POINT
# ==========================================================

# Tuple methods:
#
# count()
# index()
#
# These are built-in tuple methods.

# Most other tuple operations are performed
# using operators or built-in functions.
