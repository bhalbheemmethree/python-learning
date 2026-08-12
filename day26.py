# ==========================================================
# PYTHON DAY 26
# DICTIONARY METHODS
# ==========================================================


# ==========================================================
# keys()
# ==========================================================

# keys() returns all the keys of a dictionary.

student = {
    "name": "Bhalbheem",
    "age": 17,
    "branch": "CSE"
}

print(student.keys())

# Output:

# dict_keys(['name', 'age', 'branch'])


# ==========================================================
# values()
# ==========================================================

# values() returns all the values of a dictionary.

student = {
    "name": "Bhalbheem",
    "age": 17,
    "branch": "CSE"
}

print(student.values())

# Output:

# dict_values(['Bhalbheem', 17, 'CSE'])


# ==========================================================
# items()
# ==========================================================

# items() returns all key-value pairs
# as tuples.

student = {
    "name": "Bhalbheem",
    "age": 17,
    "branch": "CSE"
}

print(student.items())

# Output:

# dict_items([
#     ('name', 'Bhalbheem'),
#     ('age', 17),
#     ('branch', 'CSE')
# ])


# ==========================================================
# get()
# ==========================================================

# get() returns the value associated with a key.

student = {
    "name": "Bhalbheem",
    "age": 17
}

print(student.get("name"))

# Output:

# Bhalbheem


# ==========================================================
# get() WITH A MISSING KEY
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17
}

print(student.get("branch"))

# Output:

# None

# get() returns None if the key does not exist.


# ==========================================================
# get() WITH DEFAULT VALUE
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17
}

print(student.get("branch", "Not Available"))

# Output:

# Not Available


# ==========================================================
# update()
# ==========================================================

# update() adds new key-value pairs
# or changes existing values.

student = {
    "name": "Bhalbheem",
    "age": 17
}

student.update({"branch": "CSE"})

print(student)

# Output:

# {'name': 'Bhalbheem', 'age': 17, 'branch': 'CSE'}


# ==========================================================
# update() EXISTING KEY
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17
}

student.update({"age": 18})

print(student)

# Output:

# {'name': 'Bhalbheem', 'age': 18}


# ==========================================================
# pop()
# ==========================================================

# pop() removes a specified key
# and returns its value.

student = {
    "name": "Bhalbheem",
    "age": 17,
    "branch": "CSE"
}

age = student.pop("age")

print(age)
print(student)

# Output:

# 17
# {'name': 'Bhalbheem', 'branch': 'CSE'}


# ==========================================================
# pop() WITH DEFAULT VALUE
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17
}

result = student.pop("branch", "Not Available")

print(result)

# Output:

# Not Available

# If the key does not exist,
# the default value is returned.


# ==========================================================
# popitem()
# ==========================================================

# popitem() removes and returns
# the last inserted key-value pair.

student = {
    "name": "Bhalbheem",
    "age": 17,
    "branch": "CSE"
}

removed = student.popitem()

print(removed)
print(student)

# Output:

# ('branch', 'CSE')
# {'name': 'Bhalbheem', 'age': 17}


# ==========================================================
# clear()
# ==========================================================

# clear() removes all key-value pairs.

student = {
    "name": "Bhalbheem",
    "age": 17
}

student.clear()

print(student)

# Output:

# {}


# ==========================================================
# copy()
# ==========================================================

# copy() creates a copy of a dictionary.

student = {
    "name": "Bhalbheem",
    "age": 17
}

new_student = student.copy()

print(new_student)

# Output:

# {'name': 'Bhalbheem', 'age': 17}


# ==========================================================
# MODIFYING THE COPY
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17
}

new_student = student.copy()

new_student["age"] = 18

print(student)
print(new_student)

# Output:

# {'name': 'Bhalbheem', 'age': 17}
# {'name': 'Bhalbheem', 'age': 18}


# ==========================================================
# setdefault()
# ==========================================================

# setdefault() returns the value of a key
# if the key already exists.

student = {
    "name": "Bhalbheem",
    "age": 17
}

result = student.setdefault("age", 18)

print(result)
print(student)

# Output:

# 17
# {'name': 'Bhalbheem', 'age': 17}

# Existing values are not changed.


# ==========================================================
# setdefault() WITH NEW KEY
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17
}

student.setdefault("branch", "CSE")

print(student)

# Output:

# {'name': 'Bhalbheem', 'age': 17, 'branch': 'CSE'}

# If the key does not exist,
# setdefault() adds it with the given value.


# ==========================================================
# fromkeys()
# ==========================================================

# fromkeys() creates a new dictionary
# using the given keys.

keys = ["name", "age", "branch"]

student = dict.fromkeys(keys)

print(student)

# Output:

# {'name': None, 'age': None, 'branch': None}


# ==========================================================
# fromkeys() WITH A VALUE
# ==========================================================

keys = ["name", "age", "branch"]

student = dict.fromkeys(keys, "Unknown")

print(student)

# Output:

# {'name': 'Unknown', 'age': 'Unknown', 'branch': 'Unknown'}


# ==========================================================
# ITERATING THROUGH DICTIONARY KEYS
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

# By default, a for loop over a dictionary
# iterates through its keys.


# ==========================================================
# ITERATING THROUGH VALUES
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17,
    "branch": "CSE"
}

for value in student.values():
    print(value)

# Output:

# Bhalbheem
# 17
# CSE


# ==========================================================
# ITERATING THROUGH KEYS AND VALUES
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17,
    "branch": "CSE"
}

for key, value in student.items():
    print(key, value)

# Output:

# name Bhalbheem
# age 17
# branch CSE


# ==========================================================
# DICTIONARY METHODS QUICK REVISION
# ==========================================================

# keys()
# -> Returns all keys.

# values()
# -> Returns all values.

# items()
# -> Returns all key-value pairs.

# get()
# -> Returns the value of a key safely.

# update()
# -> Adds or updates key-value pairs.

# pop()
# -> Removes a specified key and returns its value.

# popitem()
# -> Removes and returns the last inserted pair.

# clear()
# -> Removes all key-value pairs.

# copy()
# -> Creates a copy of the dictionary.

# setdefault()
# -> Returns the existing value or adds the key
#    if it does not exist.

# fromkeys()
# -> Creates a dictionary using given keys.


# ==========================================================
# IMPORTANT DIFFERENCES
# ==========================================================

# get()
# -> Reads a value without removing it.

# pop()
# -> Removes a specified key.

# popitem()
# -> Removes the last inserted key-value pair.

# update()
# -> Adds or modifies key-value pairs.

# setdefault()
# -> Adds a key only if it does not already exist.


# ==========================================================
# QUICK REVISION
# ==========================================================

student = {
    "name": "Bhalbheem",
    "age": 17,
    "branch": "CSE"
}

print(student.keys())
print(student.values())
print(student.items())

print(student.get("name"))

student.update({"age": 18})

print(student)
