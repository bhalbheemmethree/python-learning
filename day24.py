# ==========================================================
# PYTHON DAY 24
# SET METHODS & OPERATIONS
# ==========================================================


# ==========================================================
# add()
# ==========================================================

# add() adds one element to a set.

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)

# Output:

# {10, 20, 30, 40}


# ==========================================================
# ADDING A DUPLICATE
# ==========================================================

numbers = {10, 20, 30}

numbers.add(20)

print(numbers)

# Output:

# {10, 20, 30}

# Sets do not store duplicate values.


# ==========================================================
# update()
# ==========================================================

# update() adds multiple elements to a set.

numbers = {10, 20, 30}

numbers.update([40, 50, 60])

print(numbers)

# Output:

# {10, 20, 30, 40, 50, 60}


# ==========================================================
# remove()
# ==========================================================

# remove() removes a specified element from a set.

numbers = {10, 20, 30, 40}

numbers.remove(30)

print(numbers)

# Output:

# {10, 20, 40}


# If the element does not exist,
# remove() raises a KeyError.


# ==========================================================
# discard()
# ==========================================================

# discard() removes a specified element
# from a set.

numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)

# Output:

# {10, 30}


# If the element does not exist,
# discard() does not raise an error.


# ==========================================================
# remove() VS discard()
# ==========================================================

numbers = {10, 20, 30}

# remove()
# numbers.remove(50)
# Raises KeyError


numbers.discard(50)

print(numbers)

# No error is raised.


# ==========================================================
# pop()
# ==========================================================

# pop() removes and returns an arbitrary
# element from a set.

numbers = {10, 20, 30}

removed = numbers.pop()

print(removed)
print(numbers)

# The removed element is not guaranteed
# to be a particular value.

# Sets are unordered.


# ==========================================================
# clear()
# ==========================================================

# clear() removes all elements from a set.

numbers = {10, 20, 30}

numbers.clear()

print(numbers)

# Output:

# set()


# ==========================================================
# UNION
# ==========================================================

# union() combines all unique elements
# from two or more sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)

print(result)

# Output:

# {1, 2, 3, 4, 5}


# ==========================================================
# UNION USING |
# ==========================================================

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1 | set2

print(result)

# Output:

# {1, 2, 3, 4, 5}


# ==========================================================
# INTERSECTION
# ==========================================================

# intersection() returns elements
# common to both sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.intersection(set2)

print(result)

# Output:

# {3, 4}


# ==========================================================
# INTERSECTION USING &
# ==========================================================

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1 & set2

print(result)

# Output:

# {3, 4}


# ==========================================================
# DIFFERENCE
# ==========================================================

# difference() returns elements that are
# present in the first set but not in the second.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.difference(set2)

print(result)

# Output:

# {1, 2}


# ==========================================================
# DIFFERENCE USING -
# ==========================================================

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1 - set2

print(result)

# Output:

# {1, 2}


# ==========================================================
# SYMMETRIC DIFFERENCE
# ==========================================================

# symmetric_difference() returns elements
# that are present in either set,
# but not in both.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.symmetric_difference(set2)

print(result)

# Output:

# {1, 2, 4, 5}


# ==========================================================
# SYMMETRIC DIFFERENCE USING ^
# ==========================================================

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1 ^ set2

print(result)

# Output:

# {1, 2, 4, 5}


# ==========================================================
# SUBSET
# ==========================================================

# issubset() checks whether all elements
# of one set are present in another set.

set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1.issubset(set2))

# Output:

# True

# set1 is a subset of set2.


# ==========================================================
# SUBSET USING <=
# ==========================================================

set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1 <= set2)

# Output:

# True


# ==========================================================
# SUPERSET
# ==========================================================

# issuperset() checks whether a set
# contains all elements of another set.

set1 = {1, 2, 3, 4}
set2 = {1, 2}

print(set1.issuperset(set2))

# Output:

# True


# ==========================================================
# SUPERSET USING >=
# ==========================================================

set1 = {1, 2, 3, 4}
set2 = {1, 2}

print(set1 >= set2)

# Output:

# True


# ==========================================================
# DISJOINT SETS
# ==========================================================

# isdisjoint() checks whether two sets
# have no elements in common.

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))

# Output:

# True


# ==========================================================
# SET METHODS QUICK REVISION
# ==========================================================

# add()
# -> Adds one element.

# update()
# -> Adds multiple elements.

# remove()
# -> Removes an element and raises an error
#    if the element does not exist.

# discard()
# -> Removes an element without raising an error
#    if it does not exist.

# pop()
# -> Removes and returns an arbitrary element.

# clear()
# -> Removes all elements.

# union()
# -> Combines unique elements.

# intersection()
# -> Returns common elements.

# difference()
# -> Returns elements present in the first set
#    but not the second.

# symmetric_difference()
# -> Returns elements present in either set
#    but not both.

# issubset()
# -> Checks whether one set is contained in another.

# issuperset()
# -> Checks whether one set contains another.

# isdisjoint()
# -> Checks whether two sets have no common elements.


# ==========================================================
# OPERATOR QUICK REVISION
# ==========================================================

# |  -> Union

# &  -> Intersection

# -  -> Difference

# ^  -> Symmetric Difference

# <= -> Subset

# >= -> Superset


# ==========================================================
# IMPORTANT DIFFERENCES
# ==========================================================

# remove() vs discard()

# remove()   -> Error if element doesn't exist
# discard()  -> No error if element doesn't exist


# union() vs intersection()

# union()        -> All unique elements
# intersection() -> Common elements


# difference() vs symmetric_difference()

# difference()           -> Elements only in first set
# symmetric_difference() -> Elements only in either set,
#                           excluding common elements
