# ==========================================================
# PYTHON DAY 38
# FILE I/O IN PYTHON
# ==========================================================


# ==========================================================
# WHAT IS FILE I/O?
# ==========================================================

# Definition:

# File I/O means File Input/Output.

# It allows a Python program to read data from files
# and write data to files.

# I/O means:

# Input  → Reading data from a file
# Output → Writing data to a file


# ==========================================================
# WHY IS FILE HANDLING NEEDED?
# ==========================================================

# Variables store data temporarily while a program is running.

# Files allow data to be stored permanently.

# Examples:

# • Saving user information
# • Storing notes
# • Saving configuration
# • Reading text files
# • Storing application data


# ==========================================================
# OPENING A FILE
# ==========================================================

# Python uses the open() function to open a file.

# Syntax:

# open(filename, mode)


# Example:

# file = open("data.txt", "r")


# ==========================================================
# FILE MODES
# ==========================================================

# Common file modes:

# "r"  → Read
# "w"  → Write
# "a"  → Append
# "x"  → Create


# ==========================================================
# READ MODE — "r"
# ==========================================================

# Definition:

# The "r" mode opens a file for reading.

# Example:

file = open("data.txt", "r")

# The file must already exist.


# ==========================================================
# WRITE MODE — "w"
# ==========================================================

# Definition:

# The "w" mode opens a file for writing.

# Example:

file = open("data.txt", "w")


# Important:

# If the file already exists, its previous contents
# are replaced.

# If the file does not exist, Python creates it.


# ==========================================================
# APPEND MODE — "a"
# ==========================================================

# Definition:

# The "a" mode opens a file for adding data at the end.

# Example:

file = open("data.txt", "a")


# Existing content is preserved.


# ==========================================================
# CREATE MODE — "x"
# ==========================================================

# Definition:

# The "x" mode creates a new file.

# Example:

file = open("newfile.txt", "x")


# If the file already exists, an error occurs.


# ==========================================================
# READING A FILE
# ==========================================================

# Example:

file = open("data.txt", "r")

content = file.read()

print(content)

file.close()


# ==========================================================
# CLOSING A FILE
# ==========================================================

# Definition:

# The close() method closes an opened file.

# Example:

file = open("data.txt", "r")

content = file.read()

print(content)

file.close()


# ==========================================================
# WHY CLOSE A FILE?
# ==========================================================

# Closing a file:

# • Releases system resources.
# • Prevents unnecessary file usage.
# • Ensures the file is properly closed.


# ==========================================================
# WRITING TO A FILE
# ==========================================================

# Example:

file = open("data.txt", "w")

file.write("Hello Python")

file.close()


# The file now contains:

# Hello Python


# ==========================================================
# WRITING MULTIPLE LINES
# ==========================================================

file = open("data.txt", "w")

file.write("Python\n")
file.write("Java\n")
file.write("SQL\n")

file.close()


# File contents:

# Python
# Java
# SQL


# ==========================================================
# APPENDING DATA
# ==========================================================

file = open("data.txt", "a")

file.write("Django\n")

file.close()


# Existing content remains,
# and Django is added at the end.


# ==========================================================
# READ AND WRITE MODES
# ==========================================================

# "r"  → Read only

# "w"  → Write only

# "a"  → Append only

# "r+" → Read and write

# "w+" → Write and read

# "a+" → Append and read


# ==========================================================
# FILE NOT FOUND
# ==========================================================

# If a file does not exist and we use "r":

# file = open("missing.txt", "r")


# Python raises:

# FileNotFoundError


# ==========================================================
# USING with TO OPEN FILES
# ==========================================================

# The with statement is the recommended way
# to work with files.

# Example:

with open("data.txt", "r") as file:

    content = file.read()

    print(content)


# The file is automatically closed
# after leaving the with block.


# ==========================================================
# WRITING USING with
# ==========================================================

with open("data.txt", "w") as file:

    file.write("Hello Python")


# The file is automatically closed.


# ==========================================================
# APPENDING USING with
# ==========================================================

with open("data.txt", "a") as file:

    file.write("\nHello again")


# ==========================================================
# FILE PATH
# ==========================================================

# A file can be opened using:

# • Relative path
# • Absolute path


# Relative path:

file = open("data.txt", "r")


# File is searched relative to
# the current working directory.


# Absolute path:

file = open("/Users/username/Documents/data.txt", "r")


# This specifies the complete location.


# ==========================================================
# RELATIVE PATH
# ==========================================================

# Example:

# project/
# │
# ├── main.py
# └── data.txt


# From main.py:

with open("data.txt", "r") as file:

    print(file.read())


# ==========================================================
# FILE ENCODING
# ==========================================================

# Files can contain different characters and languages.

# We can specify encoding while opening a file.

# Example:

with open("data.txt", "r", encoding="utf-8") as file:

    content = file.read()

    print(content)


# UTF-8 is a common text encoding.


# ==========================================================
# TEXT FILES
# ==========================================================

# Text files store readable characters.

# Examples:

# .txt
# .csv
# .py
# .html


# Example:

with open("notes.txt", "r") as file:

    print(file.read())


# ==========================================================
# BINARY FILES
# ==========================================================

# Binary files contain data that is not intended
# to be read directly as normal text.

# Examples:

# • Images
# • Videos
# • Audio
# • PDF files


# Binary modes use:

# "rb" → Read binary
# "wb" → Write binary
# "ab" → Append binary


# ==========================================================
# READING A BINARY FILE
# ==========================================================

with open("image.jpg", "rb") as file:

    data = file.read()


# ==========================================================
# COPYING A BINARY FILE
# ==========================================================

with open("image.jpg", "rb") as source:

    data = source.read()


with open("copy.jpg", "wb") as destination:

    destination.write(data)


# ==========================================================
# IMPORTANT FILE METHODS
# ==========================================================

# read()
#     → Reads file contents.

# write()
#     → Writes data to a file.

# close()
#     → Closes the file.

# More methods such as readlines(), readline(),
# seek() and tell() will be covered in the next
# two days.


# ==========================================================
# COMMON FILE MODES
# ==========================================================

# r
# → Read

# w
# → Write and replace existing content

# a
# → Add content at the end

# x
# → Create a new file

# rb
# → Read binary

# wb
# → Write binary

# ab
# → Append binary


# ==========================================================
# IMPORTANT DIFFERENCE
# ==========================================================

# "w":

file = open("data.txt", "w")

file.write("New content")

# Previous content is overwritten.


# "a":

file = open("data.txt", "a")

file.write("New content")

# Previous content is preserved.
# New content is added at the end.


# ==========================================================
# PRACTICAL EXAMPLE
# ==========================================================

# Write:

with open("students.txt", "w") as file:

    file.write("Alice\n")
    file.write("Bob\n")
    file.write("Charlie\n")


# Read:

with open("students.txt", "r") as file:

    content = file.read()

    print(content)


# Append:

with open("students.txt", "a") as file:

    file.write("David\n")


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# • File I/O allows programs to read and write files.
# • open() is used to open a file.
# • "r" is used for reading.
# • "w" is used for writing.
# • "a" is used for appending.
# • "x" is used for creating a new file.
# • close() closes an opened file.
# • with automatically manages the file.
# • File paths can be relative or absolute.
# • UTF-8 is a commonly used text encoding.
# • Binary files use modes such as rb and wb.


# ==========================================================
# QUICK REVISION
# ==========================================================

# Open:

file = open("data.txt", "r")


# Read:

content = file.read()


# Write:

file.write("Hello")


# Close:

file.close()


# Recommended:

with open("data.txt", "r") as file:

    content = file.read()


# ==========================================================
# SUMMARY
# ==========================================================

# • File I/O means File Input/Output.
# • Files provide persistent storage for data.
# • open() opens files.
# • r reads files.
# • w writes and overwrites files.
# • a appends data.
# • x creates a new file.
# • with is the preferred way to manage files.
# • Text and binary files can be handled using different modes.
