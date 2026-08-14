# ==========================================================
# PYTHON DAY 36
# OS MODULE
# ==========================================================


# ==========================================================
# WHAT IS THE os MODULE?
# ==========================================================

'''Definition:

The os module is a built-in Python module that provides
functions for interacting with the operating system.

It can be used to work with:

• Files
• Folders
• Directories
• File paths
• Environment information'''


# ==========================================================
# IMPORTING os
# ==========================================================

import os


# ==========================================================
# CURRENT WORKING DIRECTORY
# ==========================================================

'''Definition:

The current working directory (CWD) is the directory
from which the Python program is currently running.

Command:

os.getcwd()


Example:

import os

print(os.getcwd())

# Output:

# The path of the current working directory.'''


# ==========================================================
# CHANGING CURRENT WORKING DIRECTORY
# ==========================================================

'''The os.chdir() function changes the current working directory.

Example:

import os

os.chdir("/Users/username/Documents")

print(os.getcwd())'''


# ==========================================================
# LISTING FILES AND FOLDERS
# ==========================================================

'''The os.listdir() function returns the files and directories
inside a specified directory.

Example:

import os

print(os.listdir())


# This lists items in the current directory.'''


# ==========================================================
# LISTING A SPECIFIC DIRECTORY
# ==========================================================

import os

print(os.listdir("/Users/username/Documents"))


# ==========================================================
# CREATING A DIRECTORY
# ==========================================================

'''The os.mkdir() function creates a new directory.

Example:

import os

os.mkdir("my_folder")


# A folder named my_folder is created.'''


# ==========================================================
# CREATING NESTED DIRECTORIES
# ==========================================================

'''The os.makedirs() function can create multiple
directories at once.

Example:

import os

os.makedirs("project/src/files")


# Creates:

# project/
#     src/
#         files/
'''

# ==========================================================
# REMOVING A DIRECTORY
# ==========================================================

'''The os.rmdir() function removes an empty directory.

Example:

import os

os.rmdir("my_folder")


# The directory must be empty.'''


# ==========================================================
# REMOVING NESTED EMPTY DIRECTORIES
# ==========================================================

import os

os.removedirs("project/src/files")


# Removes directories from the deepest level
# when they are empty.


# ==========================================================
# CHECKING WHETHER A FILE OR DIRECTORY EXISTS
# ==========================================================

'''The os.path.exists() function checks whether
a path exists.

Example:

import os

if os.path.exists("data.txt"):

    print("File exists")

else:

    print("File does not exist")'''


# ==========================================================
# CHECKING FOR A FILE
# ==========================================================

import os

if os.path.isfile("data.txt"):

    print("It is a file")


# ==========================================================
# CHECKING FOR A DIRECTORY
# ==========================================================

import os

if os.path.isdir("my_folder"):

    print("It is a directory")


# ==========================================================
# JOINING PATHS
# ==========================================================

'''The os.path.join() function joins path components
correctly according to the operating system.

Example:

import os

path = os.path.join("project", "data", "file.txt")

print(path)'''


# ==========================================================
# GETTING FILE NAME FROM PATH
# ==========================================================

import os

path = "/Users/username/Documents/data.txt"

print(os.path.basename(path))

# Output:

# data.txt


# ==========================================================
# GETTING DIRECTORY NAME FROM PATH
# ==========================================================

import os

path = "/Users/username/Documents/data.txt"

print(os.path.dirname(path))

# Output:

# /Users/username/Documents


# ==========================================================
# SPLITTING PATH
# ==========================================================

import os

path = "/Users/username/Documents/data.txt"

result = os.path.split(path)

print(result)

# Output:

# ('/Users/username/Documents', 'data.txt')


# ==========================================================
# GETTING FILE EXTENSION
# ==========================================================

'''The os.path.splitext() function separates
the filename and extension.

Example:

import os

path = "document.txt"

name, extension = os.path.splitext(path)

print(name)
print(extension)

# Output:

# document
# .txt
'''

# ==========================================================
# RENAMING A FILE
# ==========================================================

'''The os.rename() function changes the name of a file
or directory.

Example:

import os

os.rename("old.txt", "new.txt")'''


# ==========================================================
# RENAMING A DIRECTORY
# ==========================================================

import os

os.rename("old_folder", "new_folder")


# ==========================================================
# REMOVING A FILE
# ==========================================================

'''The os.remove() function deletes a file.

Example:

import os

os.remove("data.txt")


# Be careful when using os.remove().
# The file is deleted from the filesystem.'''


# ==========================================================
# ENVIRONMENT VARIABLES
# ==========================================================

'''Definition:

Environment variables are values provided by the operating
system that can store configuration information.

Python can access them using os.environ.

Example:

import os

print(os.environ)


# This displays environment variables.'''


# ==========================================================
# GETTING AN ENVIRONMENT VARIABLE
# ==========================================================

import os

username = os.environ.get("USER")

print(username)


# On different operating systems,
# environment-variable names can differ.


# ==========================================================
# os.name
# ==========================================================

'''os.name provides information about the operating system.

Example:

import os

print(os.name)


# Common values:

# posix
# -> Unix-like systems such as Linux and macOS'''


# ==========================================================
# PATH SEPARATOR
# ==========================================================

'''Different operating systems use different path separators.

os.path.join() helps avoid manually dealing with
these differences.

Example:

import os

path = os.path.join("folder", "file.txt")

print(path)'''


# ==========================================================
# WALKING THROUGH DIRECTORIES
# ==========================================================

'''os.walk() can be used to traverse a directory tree.

Example:

import os

for root, directories, files in os.walk("."):

    print("Root:", root)
    print("Directories:", directories)
    print("Files:", files)


# It provides:

# root
# directories
# files'''


# ==========================================================
# SIMPLE FILE SEARCH
# ==========================================================

import os

for file in os.listdir():

    if file.endswith(".txt"):

        print(file)


# This prints .txt files in the current directory.


# ==========================================================
# PRACTICAL EXAMPLE
# ==========================================================

import os

folder = "documents"

if not os.path.exists(folder):

    os.mkdir(folder)

print("Folder ready")


# If the folder doesn't exist,
# it is created.


# ==========================================================
# IMPORTANT os FUNCTIONS
# ==========================================================

os.getcwd()
# Get current working directory.

os.chdir()
# Change current working directory.

os.listdir()
# List files and directories.

os.mkdir()
# Create a directory.

os.makedirs()
# Create nested directories.

os.rmdir()
# Remove an empty directory.

os.remove()
# Remove a file.

os.rename()
# Rename a file or directory.

os.path.exists()
# Check whether a path exists.

os.path.isfile()
# Check whether a path is a file.

os.path.isdir()
# Check whether a path is a directory.

os.path.join()
# Join path components.

os.path.basename()
# Get filename from a path.

os.path.dirname()
# Get directory from a path.

os.path.split()
# Split path into directory and filename.

os.path.splitext()
# Split filename and extension.

os.walk()
# Traverse directory trees.


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

'''• os is a built-in Python module.
• It allows Python to interact with the operating system.
• os.getcwd() gets the current directory.
• os.chdir() changes the current directory.
• os.listdir() lists directory contents.
• os.mkdir() creates a directory.
• os.remove() removes a file.
• os.rename() renames a file or directory.
• os.path provides useful path-related functions.
• os.walk() can traverse directory structures.'''


# ==========================================================
# QUICK REVISION
# ==========================================================

import os

os.getcwd()
# Current directory

os.listdir()
# List directory contents

os.mkdir("folder")
# Create folder

os.remove("file.txt")
# Delete file

os.rename("old.txt", "new.txt")
# Rename file

os.path.exists("file.txt")
# Check existence

os.path.isfile("file.txt")
# Check file

os.path.isdir("folder")
# Check directory

os.path.join("folder", "file.txt")
# Join paths


# ==========================================================
# SUMMARY
# ==========================================================

# • os allows Python to interact with the operating system.
# • It can work with files, folders and directories.
# • os.path provides functions for handling paths.
# • os can create, remove and rename filesystem items.
# • os.environ provides access to environment variables.
# • os.walk() can traverse directory structures.
