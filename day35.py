# ==========================================================
# PYTHON DAY 35
# if __name__ == "__main__"
# ==========================================================


# ==========================================================
# WHAT IS __name__?
# ==========================================================

'''Definition:

__name__ is a special built-in variable in Python that
represents the name of the current module.

When a Python file is run directly, Python sets:

__name__ = "__main__"'''


# ==========================================================
# BASIC EXAMPLE
# ==========================================================

print(__name__)

# If this file is run directly:

# Output:

# __main__


# ==========================================================
# WHAT IS __main__?
# ==========================================================

'''Definition:

"__main__" is the special value assigned to __name__
when a Python file is executed directly.'''


# ==========================================================
# if __name__ == "__main__"
# ==========================================================

# Syntax:

if __name__ == "__main__":

    # Code to execute when this file
    # is run directly


# ==========================================================
# BASIC EXAMPLE
# ==========================================================

# def greet():

    print("Hello Python")


if __name__ == "__main__":

   ''' greet()'''

# Output when this file is run directly:

# Hello Python


# ==========================================================
# WHY DO WE USE IT?
# ==========================================================

'''It allows us to control which code runs when a Python
file is:

• Run directly
• Imported as a module'''


# ==========================================================
# DIRECT EXECUTION
# ==========================================================

# Suppose we have:

# calculator.py

def add(a, b):

    return a + b


if __name__ == "__main__":

    print(add(10, 20))


# If we run:

# python calculator.py


# Output:

# 30


# ==========================================================
# IMPORTING THE FILE
# ==========================================================

# Suppose another file contains:

# main.py

# import calculator

# print(calculator.add(5, 10))
#

# When calculator.py is imported:

# Its function is available.

# But this code:

if __name__ == "__main__":

    print(add(10, 20))

# does NOT execute.

# Why?

# Because when calculator.py is imported:

# calculator.__name__ = "calculator"

# Therefore:

# calculator.__name__ == "__main__"

# is False.


# ==========================================================
# DIRECT RUN VS IMPORT
# ==========================================================

# When directly running:

# python calculator.py

# Python sets:

__name__ = "__main__"


# When importing:

# import calculator

# Python sets:

# calculator.__name__ = "calculator"


# ==========================================================
# COMPLETE EXAMPLE
# ==========================================================

# File: calculator.py

def add(a, b):

    return a + b


print("Calculator module loaded")


if __name__ == "__main__":

    print(add(10, 20))


# If directly executed:

# Output:

# Calculator module loaded
# 30


# If imported:

# import calculator

# Output:

# Calculator module loaded

# The add() function is available,
# but the code inside the if block does not execute.


# ==========================================================
# IMPORTANT DIFFERENCE
# ==========================================================

# Code outside the block:

print("Hello")

# runs when the module is imported too.

# Code inside:

if __name__ == "__main__":

    print("Hello")

# runs only when the file is executed directly.


# ==========================================================
# USING A MAIN FUNCTION
# ==========================================================

def main():

    print("Program started")

    number = 10

    print(number)


if __name__ == "__main__":

    main()


# This is a common Python program structure.


# ==========================================================
# WHY USE A main() FUNCTION?
# ==========================================================

# It keeps the main program logic organized.

# Example:

def add(a, b):

    return a + b


def main():

    result = add(10, 20)

    print(result)


if __name__ == "__main__":

    main()


# ==========================================================
# __name__ VS __main__
# ==========================================================

__name__

# → Special variable containing the current module's name.


"__main__"

# → Special value used when the file is executed directly.


# ==========================================================
# IMPORTANT POINTS
# ==========================================================

'''• __name__ is a special Python variable.
• When a file is executed directly, __name__ is "__main__".
• When a file is imported, __name__ contains the module name.
• The if __name__ == "__main__": block runs only when
  the file is executed directly.
• It prevents certain code from running automatically
  when the file is imported.
• It is commonly used to define the main entry point
  of a Python program.'''


# ==========================================================
# QUICK REVISION
# ==========================================================

# if __name__ == "__main__":

    # print("Run directly")


# Direct execution:

# Runs the block.


# Import:

# Does not run the block.


# ==========================================================
# SUMMARY
# ==========================================================

# • __name__ identifies the current module.
# • "__main__" means the file is being executed directly.
# • if __name__ == "__main__": controls direct execution.
# • It is useful when a file can work both as a module
#   and as a standalone program.
# • It is commonly used with a main() function.
