# ==========================================================
# PYTHON DAY 39
# FILE METHODS
# ==========================================================


# ==========================================================
# read()
# ==========================================================

# Definition:

# The read() method is used to read the contents of a file.

# Example:

with open("data.txt", "r") as file:

    content = file.read()

    print(content)


# It reads the entire file.


# ==========================================================
# read() WITH NUMBER OF CHARACTERS
# ==========================================================

# The read() method can also accept a number.

# Example:

with open("data.txt", "r") as file:

    content = file.read(5)

    print(content)


# It reads the first 5 characters.


# ==========================================================
# readline()
# ==========================================================

# Definition:

# The readline() method reads one line from a file.

# Example:

with open("data.txt", "r") as file:

    line = file.readline()

    print(line)


# It reads the first line.


# ==========================================================
# READING MULTIPLE LINES USING readline()
# ==========================================================

with open("data.txt", "r") as file:

    print(file.readline())
    print(file.readline())
    print(file.readline())


# Each call reads the next line.


# ==========================================================
# readlines()
# ==========================================================

# Definition:

# The readlines() method reads all lines from a file
# and returns them as a list.

# Example:

with open("data.txt", "r") as file:

    lines = file.readlines()

    print(lines)


# Example output:

# ['Python\n', 'Java\n', 'SQL\n']


# ==========================================================
# read() VS readline() VS readlines()
# ==========================================================

# read()

# → Reads the entire file.


# readline()

# → Reads one line at a time.


# readlines()

# → Reads all lines and returns them as a list.


# ==========================================================
# EXAMPLE FILE
# ==========================================================

# Suppose data.txt contains:

# Python
# Java
# SQL


# read():

with open("data.txt", "r") as file:

    print(file.read())


# Output:

# Python
# Java
# SQL


# ==========================================================
# readline()
# ==========================================================

with open("data.txt", "r") as file:

    print(file.readline())

    print(file.readline())


# Output:

# Python
# Java


# ==========================================================
# readlines()
# ==========================================================

with open("data.txt", "r") as file:

    lines = file.readlines()

    print(lines)


# Output:

# ['Python\n', 'Java\n', 'SQL\n']


# ==========================================================
# writelines()
# ==========================================================

# Definition:

# The writelines() method writes multiple strings to a file.

# Example:

lines = [
    "Python\n",
    "Java\n",
    "SQL\n"
]

with open("data.txt", "w") as file:

    file.writelines(lines)


# Important:

# writelines() does NOT automatically add \n
# between strings.

# Therefore, newline characters must be included
# when required.


# ==========================================================
# write()
# ==========================================================

# Definition:

# The write() method writes a string to a file.

# Example:

with open("data.txt", "w") as file:

    file.write("Hello Python")


# ==========================================================
# write() RETURN VALUE
# ==========================================================

# write() returns the number of characters written.

# Example:

with open("data.txt", "w") as file:

    count = file.write("Python")

    print(count)

# Output:

# 6


# ==========================================================
# flush()
# ==========================================================

# Definition:

# The flush() method forces buffered data to be written
# to the file immediately.

# Example:

file = open("data.txt", "w")

file.write("Hello")

file.flush()

file.close()


# Usually, when using with, Python handles
# the file closing automatically.


# ==========================================================
# close()
# ==========================================================

# Definition:

# The close() method closes an opened file.

# Example:

file = open("data.txt", "r")

print(file.read())

file.close()


# ==========================================================
# CHECKING WHETHER FILE IS CLOSED
# ==========================================================

# Example:

file = open("data.txt", "r")

print(file.closed)

file.close()

print(file.closed)


# Output:

# False
# True


# ==========================================================
# CHECKING FILE MODE
# ==========================================================

# The mode attribute tells us how the file was opened.

# Example:

file = open("data.txt", "r")

print(file.mode)

file.close()

# Output:

# r


# ==========================================================
# FILE NAME
# ==========================================================

# The name attribute gives the name of the file.

# Example:

file = open("data.txt", "r")

print(file.name)

file.close()

# Output:

# data.txt


# ==========================================================
# FILE ITERATION
# ==========================================================

# A file can be directly used in a for loop
# to read it line by line.

# Example:

with open("data.txt", "r") as file:

    for line in file:

        print(line)


# This is memory-efficient for reading
# large text files line by line.


# ==========================================================
# REMOVING EXTRA NEWLINE
# ==========================================================

# When reading lines, each line may already contain \n.

# Example:

with open("data.txt", "r") as file:

    for line in file:

        print(line.strip())


# strip() removes surrounding whitespace,
# including the newline character.


# ==========================================================
# readline() AT END OF FILE
# ==========================================================

# If readline() is called after reaching the end
# of the file, it returns an empty string.

# Example:

with open("data.txt", "r") as file:

    print(file.readline())
    print(file.readline())
    print(file.readline())


# If there are no more lines,
# readline() returns:

# ""


# ==========================================================
# read() AT END OF FILE
# ==========================================================

# After the entire file has already been read,
# another read() normally returns an empty string.

# Example:

with open("data.txt", "r") as file:

    print(file.read())

    print(file.read())

# The second read() returns:

# ""


# ==========================================================
# FILE POINTER
# ==========================================================

# Definition:

# A file pointer represents the current position
# inside an opened file.

# When data is read, the file pointer moves forward.

# Example:

with open("data.txt", "r") as file:

    print(file.read(5))

    print(file.read(5))


# The second read() continues from where
# the first read() stopped.


# More detailed file-pointer control using
# seek() and tell() will be covered in Day 40.


# ==========================================================
# IMPORTANT FILE METHODS
# ==========================================================

# read()
# → Reads data from a file.

# readline()
# → Reads one line.

# readlines()
# → Reads all lines into a list.

# write()
# → Writes a string.

# writelines()
# → Writes multiple strings.

# flush()
# → Flushes buffered data.

# close()
# → Closes the file.


# ==========================================================
# IMPORTANT FILE ATTRIBUTES
# ==========================================================

# file.name
# → File name.

# file.mode
# → File opening mode.

# file.closed
# → Whether the file is closed.


# ==========================================================
# PRACTICAL EXAMPLE
# ==========================================================

with open("students.txt", "r") as file:

    first_line = file.readline()

    remaining_lines = file.readlines()

    print("First:", first_line)
    print("Remaining:", remaining_lines)


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# • read() reads the entire file or a specified number
#   of characters.
# • readline() reads one line.
# • readlines() returns all lines as a list.
# • write() writes a string.
# • writelines() writes multiple strings.
# • write() returns the number of characters written.
# • A file has a current position called the file pointer.
# • Files can be iterated line by line using a for loop.
# • close() closes the file.
# • with automatically closes the file.


# ==========================================================
# QUICK REVISION
# ==========================================================

# read()
# → Entire file / specified characters


# readline()
# → One line


# readlines()
# → All lines as a list


# write()
# → Write one string


# writelines()
# → Write multiple strings


# close()
# → Close file


# file.name
# → File name


# file.mode
# → File mode


# file.closed
# → Closed status


# ==========================================================
# SUMMARY
# ==========================================================

# • read() reads file contents.
# • readline() reads one line at a time.
# • readlines() reads all lines into a list.
# • write() writes strings to a file.
# • writelines() writes multiple strings.
# • Files can be processed line by line using a loop.
# • The file pointer tracks the current reading position.
# • seek() and tell() are used to control/check the
#   file position and will be covered next.
