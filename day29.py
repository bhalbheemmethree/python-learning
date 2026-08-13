# ==========================================================
# PYTHON DAY 29
# FINALLY KEYWORD
# ==========================================================


# ==========================================================
# WHAT IS FINALLY?
# ==========================================================

'''Definition:

The finally block is used to execute code regardless of
whether an exception occurs or not.

The finally block is used with try and except.'''


# ==========================================================
# BASIC SYNTAX
# ==========================================================

# try:

    # Code that may cause an exception

# except:

    # Code to handle the exception

# finally:

    # Code that always executes


# ==========================================================
# BASIC EXAMPLE
# ==========================================================

try:

    number = 10 / 2

except ZeroDivisionError:

    print("Cannot divide by zero")

finally:

    print("This always executes")

# Output:

# This always executes


# ==========================================================
# FINALLY WHEN EXCEPTION OCCURS
# ==========================================================

try:

    number = 10 / 0

except ZeroDivisionError:

    print("Cannot divide by zero")

finally:

    print("Finally block executed")

# Output:

# Cannot divide by zero
# Finally block executed


# ==========================================================
# FINALLY WHEN NO EXCEPTION OCCURS
# ==========================================================

try:

    number = 10 / 2

    print(number)

except ZeroDivisionError:

    print("Cannot divide by zero")

finally:

    print("Program finished")

# Output:

# 5.0
# Program finished


# ==========================================================
# FINALLY WITH USER INPUT
# ==========================================================

try:

    number = int(input("Enter a number: "))

    print("Number:", number)

except ValueError:

    print("Invalid input")

finally:

    print("Input operation completed")


# ==========================================================
# FINALLY WITH FILE HANDLING
# ==========================================================

file = None

try:

    file = open("data.txt", "r")

    content = file.read()

    print(content)

except FileNotFoundError:

    print("File not found")

finally:

    if file is not None:

        file.close()

    print("File operation completed")


# The finally block is commonly useful for
# cleanup operations such as closing resources.


# ==========================================================
# WHY IS FINALLY NEEDED?
# ==========================================================

'''The finally block is useful when some code must execute
whether an exception occurs or not.'''

# Common uses:

# • Closing files
# • Closing connections
# • Releasing resources
# • Cleanup operations


# ==========================================================
# TRY, EXCEPT AND FINALLY
# ==========================================================

try:

    number = 10 / 0

except ZeroDivisionError:

    print("Error occurred")

finally:

    print("Cleanup completed")

# Output:

# Error occurred
# Cleanup completed


# ==========================================================
# TRY AND FINALLY WITHOUT EXCEPT
# ==========================================================

# finally can also be used directly with try.

try:

    print("Trying something")

finally:

    print("Finally executed")

# Output:

# Trying something
# Finally executed


# ==========================================================
# TRY, EXCEPT, ELSE AND FINALLY
# ==========================================================

# All four blocks can be used together.

try:

    number = 10 / 2

except ZeroDivisionError:

    print("Error occurred")

else:

    print("No exception occurred")

finally:

    print("Execution completed")

# Output:

# No exception occurred
# Execution completed


# ==========================================================
# ORDER OF EXECUTION
# ==========================================================

# When no exception occurs:

# try
#   ↓
# else
#   ↓
# finally


# When an exception occurs and is handled:

# try
#   ↓
# except
#   ↓
# finally


# ==========================================================
# FINALLY WITH RETURN
# ==========================================================

def example():

    try:

        return 10

    finally:

        print("Finally executed")


result = example()

print(result)

# Output:

# Finally executed
# 10

# The finally block executes before the function returns.


# ==========================================================
# IMPORTANT POINT
# ==========================================================

# finally normally executes whether:
#
# • An exception occurs
# • No exception occurs
# • An exception is handled
# • A return statement is used


# ==========================================================
# FINALLY VS EXCEPT
# ==========================================================

# except:

# Handles an exception.

# finally:

# Executes cleanup code regardless
# of whether an exception occurs.


# ==========================================================
# FINALLY VS ELSE
# ==========================================================

# else:

# Executes only when no exception occurs.

# finally:

# Executes regardless of whether
# an exception occurs.


# ==========================================================
# QUICK REVISION
# ==========================================================

# try
# -> Contains potentially risky code.

# except
# -> Handles an exception.

# else
# -> Executes when no exception occurs.

# finally
# -> Executes regardless of the result.


# ==========================================================
# SUMMARY
# ==========================================================

# • finally is used with exception handling.
# • finally executes whether an exception occurs or not.
# • finally is commonly used for cleanup.
# • It can be used with try and except.
# • It can also be used with try without except.
# • finally executes even when return is used.
# • else runs only when there is no exception.
# • finally normally runs in both cases.
# ============================================