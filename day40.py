# ==========================================================
# PYTHON DAY 40
# seek(), tell() AND OTHER FILE FUNCTIONS
# ==========================================================


# ==========================================================
# WHAT IS A FILE POINTER?
# ==========================================================

# Definition:

# A file pointer represents the current position
# from which data will be read or written in a file.

# When we read data, the file pointer moves forward.

# Example:

with open("data.txt", "r") as file:

    print(file.read(5))

    print(file.read(5))


# The second read() continues from the current
# file pointer position.


# ==========================================================
# tell()
# ==========================================================

# Definition:

# The tell() method returns the current position
# of the file pointer.

# Syntax:

file.tell()


# ==========================================================
# BASIC EXAMPLE
# ==========================================================

with open("data.txt", "r") as file:

    print(file.tell())

    file.read(5)

    print(file.tell())


# The position changes after reading characters.


# ==========================================================
# EXAMPLE
# ==========================================================

# Suppose data.txt contains:

# Python


with open("data.txt", "r") as file:

    print(file.tell())

    file.read(2)

    print(file.tell())

# Output:

# 0
# 2


# The pointer started at position 0
# and moved after reading 2 characters.


# ==========================================================
# seek()
# ==========================================================

# Definition:

# The seek() method changes the current position
# of the file pointer.

# Syntax:

# file.seek(position)


# ==========================================================
# BASIC EXAMPLE
# ==========================================================

with open("data.txt", "r") as file:

    file.seek(5)

    print(file.read())


# The pointer moves to position 5
# before reading.


# ==========================================================
# seek(0)
# ==========================================================

# seek(0) moves the file pointer back to the beginning.

# Example:

with open("data.txt", "r") as file:

    print(file.read(5))

    file.seek(0)

    print(file.read(5))


# The same first 5 characters are read again.


# ==========================================================
# seek() AND tell() TOGETHER
# ==========================================================

with open("data.txt", "r") as file:

    print(file.tell())

    file.seek(5)

    print(file.tell())

    file.seek(0)

    print(file.tell())


# Output:

# 0
# 5
# 0


# ==========================================================
# READING FROM A SPECIFIC POSITION
# ==========================================================

# Suppose data.txt contains:

# Python Programming


# Example:

with open("data.txt", "r") as file:

    file.seek(7)

    print(file.read())


# The file is read starting from position 7.


# ==========================================================
# READING THE SAME FILE AGAIN
# ==========================================================

with open("data.txt", "r") as file:

    print(file.read())

    file.seek(0)

    print(file.read())


# First read:
# Reads the complete file.

# seek(0):
# Moves pointer back to the beginning.

# Second read:
# Reads the complete file again.


# ==========================================================
# SEEK AFTER READ
# ==========================================================

with open("data.txt", "r") as file:

    file.read(5)

    file.seek(0)

    print(file.read(5))


# After reading 5 characters,
# seek(0) moves the pointer back.


# ==========================================================
# seek() WITH WRITE MODE
# ==========================================================

# seek() can also be used when working with files
# opened in modes that allow writing.

# Example:

with open("data.txt", "r+") as file:

    file.seek(0)

    file.write("Hello")


# r+ allows both reading and writing.


# ==========================================================
# OTHER FILE FUNCTION — truncate()
# ==========================================================

# Definition:

# The truncate() method is used to reduce or change
# the size of a file.

# Example:

with open("data.txt", "w") as file:

    file.write("Python Programming")

    file.truncate(6)


# The file is shortened to the specified size.


# ==========================================================
# truncate() WITHOUT SIZE
# ==========================================================

# If truncate() is called without a size,
# the file is truncated at the current file position.

# Example:

with open("data.txt", "w") as file:

    file.write("Hello Python")

    file.truncate()


# The file is truncated at the current position.


# ==========================================================
# flush()
# ==========================================================

# Definition:

# The flush() method forces buffered data to be written
# to the underlying file.

# Example:

file = open("data.txt", "w")

file.write("Hello")

file.flush()

file.close()


# ==========================================================
# fileno()
# ==========================================================

# Definition:

# The fileno() method returns the file descriptor
# associated with the opened file.

# Example:

with open("data.txt", "r") as file:

    print(file.fileno())


# The exact number depends on the operating system
# and the running program.


# ==========================================================
# readable()
# ==========================================================

# Definition:

# The readable() method checks whether the file
# can be read.

# Example:

with open("data.txt", "r") as file:

    print(file.readable())

# Output:

# True


# ==========================================================
# writable()
# ==========================================================

# Definition:

# The writable() method checks whether the file
# can be written to.

# Example:

with open("data.txt", "w") as file:

    print(file.writable())

# Output:

# True


# ==========================================================
# SEEKABLE()
# ==========================================================

# Definition:

# The seekable() method checks whether the file
# supports changing its position using seek().

# Example:

with open("data.txt", "r") as file:

    print(file.seekable())


# ==========================================================
# FILE POINTER EXAMPLE
# ==========================================================

with open("data.txt", "r") as file:

    print("Position:", file.tell())

    file.read(10)

    print("Position:", file.tell())

    file.seek(0)

    print("Position:", file.tell())


# ==========================================================
# PRACTICAL EXAMPLE
# ==========================================================

with open("data.txt", "r") as file:

    # Read first 5 characters
    first = file.read(5)

    print(first)

    # Check current position
    print(file.tell())

    # Move to beginning
    file.seek(0)

    # Read again
    print(file.read(5))


# ==========================================================
# IMPORTANT DIFFERENCE
# ==========================================================

# tell()

# → Tells us where the file pointer currently is.


# seek()

# → Moves the file pointer to a specified position.


# ==========================================================
# FILE FUNCTIONS / METHODS
# ==========================================================

# read()
# → Reads data.

# readline()
# → Reads one line.

# readlines()
# → Reads all lines.

# write()
# → Writes data.

# writelines()
# → Writes multiple strings.

# seek()
# → Moves file pointer.

# tell()
# → Returns current file pointer position.

# truncate()
# → Changes file size.

# flush()
# → Flushes buffered data.

# close()
# → Closes the file.


# ==========================================================
# FILE CHECKING METHODS
# ==========================================================

# readable()
# → Checks whether file can be read.

# writable()
# → Checks whether file can be written.

# seekable()
# → Checks whether file supports seeking.


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

# • A file pointer represents the current position in a file.
# • tell() returns the current pointer position.
# • seek() changes the pointer position.
# • seek(0) moves the pointer to the beginning.
# • truncate() changes the size of a file.
# • flush() writes buffered data to the file.
# • readable() checks read capability.
# • writable() checks write capability.
# • seekable() checks whether the file supports seeking.


# ==========================================================
# QUICK REVISION
# ==========================================================

# tell()
# → "Where am I?"


# seek()
# → "Move me here."


# Example:

file.tell()

file.seek(0)


# ==========================================================
# SUMMARY
# ==========================================================

# • tell() tells the current file position.
# • seek() moves the file pointer.
# • seek(0) returns to the beginning.
# • truncate() changes file size.
# • flush() forces buffered data to be written.
# • readable(), writable() and seekable() check
#   file capabilities.
