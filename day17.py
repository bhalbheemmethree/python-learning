# ==========================================================
# PYTHON DAY 17
# LIST METHODS
# ==========================================================


# ==========================================================
# append()
# ==========================================================

# append() adds one element to the end of a list.

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

# Output

# [10, 20, 30, 40]


# ==========================================================
# append() WITH DIFFERENT DATA TYPES
# ==========================================================

data = [10, 20]

data.append("Python")

print(data)

# Output

# [10, 20, 'Python']


# ==========================================================
# append() ADDS ONLY ONE ELEMENT
# ==========================================================

numbers = [1, 2, 3]

numbers.append([4, 5])

print(numbers)

# Output

# [1, 2, 3, [4, 5]]

# append() adds the entire [4, 5] as one element.


# ==========================================================
# insert()
# ==========================================================

# insert() adds an element at a specific index.

numbers = [10, 20, 30]

numbers.insert(1, 100)

print(numbers)

# Output

# [10, 100, 20, 30]

# Syntax:

# list.insert(index, value)


# ==========================================================
# extend()
# ==========================================================

# extend() adds multiple elements to the end
# of a list.

numbers = [1, 2, 3]

numbers.extend([4, 5, 6])

print(numbers)

# Output

# [1, 2, 3, 4, 5, 6]


# ==========================================================
# append() VS extend()
# ==========================================================

numbers = [1, 2, 3]

numbers.append([4, 5])

print(numbers)

# Output

# [1, 2, 3, [4, 5]]


numbers = [1, 2, 3]

numbers.extend([4, 5])

print(numbers)

# Output

# [1, 2, 3, 4, 5]

# append() -> Adds the value as one element.

# extend() -> Adds each element separately.


# ==========================================================
# remove()
# ==========================================================

# remove() removes the first occurrence
# of a specified value.

numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)

# Output

# [10, 30, 20]

# Only the first 20 is removed.


# ==========================================================
# remove() WITH A VALUE THAT DOES NOT EXIST
# ==========================================================

numbers = [10, 20, 30]

# numbers.remove(50)

# This raises a ValueError because
# 50 is not present in the list.


# ==========================================================
# pop()
# ==========================================================

# pop() removes and returns an element
# from the list.

numbers = [10, 20, 30]

numbers.pop()

print(numbers)

# Output

# [10, 20]

# By default, pop() removes the last element.


# ==========================================================
# pop() WITH INDEX
# ==========================================================

numbers = [10, 20, 30, 40]

numbers.pop(1)

print(numbers)

# Output

# [10, 30, 40]

# pop(1) removes the element at index 1.


# ==========================================================
# STORING THE VALUE REMOVED BY pop()
# ==========================================================

numbers = [10, 20, 30]

removed = numbers.pop()

print(removed)
print(numbers)

# Output

# 30
# [10, 20]


# ==========================================================
# clear()
# ==========================================================

# clear() removes all elements from the list.

numbers = [10, 20, 30]

numbers.clear()

print(numbers)

# Output

# []


# ==========================================================
# index()
# ==========================================================

# index() returns the index of the first occurrence
# of a specified value.

numbers = [10, 20, 30, 20]

print(numbers.index(20))

# Output

# 1

# The first 20 is at index 1.


# ==========================================================
# count()
# ==========================================================

# count() returns how many times
# a value appears in the list.

numbers = [10, 20, 20, 30, 20]

print(numbers.count(20))

# Output

# 3


# ==========================================================
# sort()
# ==========================================================

# sort() arranges the list in ascending order.

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

# Output

# [10, 20, 30, 40]


# ==========================================================
# sort() IN DESCENDING ORDER
# ==========================================================

numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)

# Output

# [40, 30, 20, 10]


# ==========================================================
# reverse()
# ==========================================================

# reverse() reverses the current order
# of the list.

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)

# Output

# [40, 30, 20, 10]

# reverse() does not sort the list.
# It simply reverses its current order.


# ==========================================================
# copy()
# ==========================================================

# copy() creates a copy of a list.

numbers = [10, 20, 30]

new_numbers = numbers.copy()

print(new_numbers)

# Output

# [10, 20, 30]


# ==========================================================
# MODIFYING THE COPY
# ==========================================================

numbers = [10, 20, 30]

new_numbers = numbers.copy()

new_numbers.append(40)

print(numbers)
print(new_numbers)

# Output

# [10, 20, 30]
# [10, 20, 30, 40]

# The copied list can be changed independently.


# ==========================================================
# QUICK REVISION
# ==========================================================

# append(value)
# -> Adds one element at the end.

# insert(index, value)
# -> Adds an element at a specific position.

# extend(iterable)
# -> Adds multiple elements.

# remove(value)
# -> Removes the first occurrence of a value.

# pop()
# -> Removes and returns the last element.

# pop(index)
# -> Removes and returns the element at an index.

# clear()
# -> Removes all elements.

# index(value)
# -> Returns the index of the first occurrence.

# count(value)
# -> Counts how many times a value occurs.

# sort()
# -> Sorts the list in ascending order.

# sort(reverse=True)
# -> Sorts the list in descending order.

# reverse()
# -> Reverses the current order.

# copy()
# -> Creates a copy of the list.
