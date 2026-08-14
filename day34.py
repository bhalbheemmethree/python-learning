# ==========================================================
# PYTHON DAY 34
# HOW IMPORT WORKS
# ==========================================================


# ==========================================================
# WHAT IS IMPORT?
# ==========================================================

# Definition:

'''The import statement is used to bring code from another
Python module into the current program.

A module is usually a Python file containing code such as:

• Variables
• Functions
• Classes
• Statements
'''

# ==========================================================
# WHAT IS A MODULE?
# ==========================================================

'''Definition:

A module is a Python file (.py) that contains reusable code.

Example:

math_utils.py

def add(a, b):

    return a + b


# Another file can import it and use the function.'''


# ==========================================================
# BASIC IMPORT
# ==========================================================

'''Suppose we have:

math_utils.py

def add(a, b):

    return a + b


# main.py

import math_utils

result = math_utils.add(10, 20)

print(result)

# Output:

# 30
'''

# ==========================================================
# HOW IMPORT WORKS
# ==========================================================

'''When Python sees:

import math_utils

Python:

1. Searches for the module.
2. Finds the module.
3. Executes the module code.
4. Creates a module object.
5. Makes it available to the current program.

After importing, we can access its contents.'''


# ==========================================================
# ACCESSING MODULE CONTENT
# ==========================================================

import math

print(math.sqrt(25))

# Output:

# 5.0

# sqrt() belongs to the math module.


# ==========================================================
# IMPORTING SPECIFIC ITEMS
# ==========================================================

from math import sqrt

print(sqrt(25))

# Output:

# 5.0

# Now sqrt() can be used directly
# without writing math.sqrt().


# ==========================================================
# IMPORTING MULTIPLE ITEMS
# ==========================================================

from math import sqrt, pi

print(sqrt(16))
print(pi)


# ==========================================================
# IMPORT ALL CONTENT
# ==========================================================

from math import *

print(sqrt(25))
print(pi)

# However, using '*' is generally discouraged
# because it can make it unclear where names came from.


# ==========================================================
# USING AS
# ==========================================================

'''Definition:

The as keyword gives an imported module or item
a different name.

Example:

import math as m

print(m.sqrt(25))

# Output:

# 5.0
'''

# ==========================================================
# IMPORTING A FUNCTION WITH AS
# ==========================================================

from math import sqrt as square_root

print(square_root(36))

# Output:

# 6.0


# ==========================================================
# STANDARD LIBRARY MODULES
# ==========================================================

'''Python provides many built-in modules.

Examples:

• math
• random
• os
• sys
• datetime
'''

# ==========================================================
# MATH MODULE
# ==========================================================

import math

print(math.sqrt(16))
print(math.pow(2, 3))

# Output:

# 4.0
# 8.0


# ==========================================================
# RANDOM MODULE
# ==========================================================

import random

number = random.randint(1, 10)

print(number)

# A random integer between 1 and 10 is generated.


# ==========================================================
# IMPORTING YOUR OWN MODULE
# ==========================================================

'''File 1:

calculator.py

def add(a, b):

    return a + b

def subtract(a, b):

    return a - b


File 2:

main.py

import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))

# Output:

# 15
# 5
'''


# ==========================================================
# MODULE CODE EXECUTION
# ==========================================================

# Suppose:

test.py

print("Module loaded")


# main.py

import test

print("Main program")


# Output:

# Module loaded
# Main program


# When test is imported, its top-level code executes.


# ==========================================================
# IMPORT HAPPENS ONLY ONCE
# ==========================================================
'''When a module is imported for the first time,
Python loads and executes it.

If the same module is imported again during the
same program execution, Python normally reuses the
already-loaded module rather than executing it again.'''


# ==========================================================
# IMPORTING THE SAME MODULE
# ==========================================================

import math
import math

print(math.sqrt(25))

# The repeated import does not normally execute
# the module again.


# ==========================================================
# MODULE SEARCH
# ==========================================================

'''When Python imports a module, it searches for it
in locations available through Python's module search path.

The search path includes locations such as:

• The current/project directory
• Standard library locations
• Installed package locations
'''

# ==========================================================
# sys.path
# ==========================================================

'''The sys module provides information about Python's
module search path.

Example:

import sys

print(sys.path)

# This displays the locations Python searches
# when importing modules.'''


# ==========================================================
# MODULE NOT FOUND
# ==========================================================

# If Python cannot find the requested module:

# import something_that_does_not_exist

# Python raises:

# ModuleNotFoundError


# ==========================================================
# IMPORTERROR
# ==========================================================

'''ImportError occurs when Python cannot import
a requested name or module correctly.

Example:

from math import something_that_does_not_exist

# This results in an ImportError.'''


# ==========================================================
# MODULE VS PACKAGE
# ==========================================================

# Module:

# A Python file containing reusable code.

# Example:

# calculator.py


# Package:

# A directory that organizes related Python modules.


# ==========================================================
# IMPORTING FROM A PACKAGE
# ==========================================================

'''Example structure:

myproject/
│
├── main.py
│
└── tools/
    ├── __init__.py
    └── calculator.py


# main.py

from tools import calculator

print(calculator.add(10, 20))
'''


# ==========================================================
# __init__.py
# ==========================================================

'''Definition:

__init__.py is a file traditionally used to mark
a directory as a Python package and can also contain
package initialization code.

Modern Python can also recognize certain directories
as namespace packages without __init__.py.'''


# ==========================================================
# IMPORT STATEMENT TYPES
# ==========================================================

# 1. Import entire module:

import math


# 2. Import specific item:

from math import sqrt


# 3. Import with alias:

import math as m


# 4. Import specific item with alias:

from math import sqrt as square_root


# ==========================================================
# WHY USE MODULES?
# ==========================================================

'''Modules help us:

• Organize code.
• Reuse code.
• Keep programs smaller and cleaner.
• Separate different parts of a project.
• Avoid writing the same code repeatedly.
'''

# ==========================================================
# IMPORTANT POINTS
# ==========================================================

'''• A module is a Python file containing reusable code.
• import loads a module into the current program.
• from ... import ... imports specific items.
• as creates an alias.
• Python executes a module's top-level code when it is
  first imported.
• Imported modules are normally loaded only once per
  program execution.
• Python searches specific locations to find modules.
• ModuleNotFoundError occurs when a module cannot be found.
• ImportError can occur when a requested import cannot
  be performed.
'''

# ==========================================================
# QUICK REVISION
# ==========================================================

import math

# Import module.

from math import sqrt

# Import specific item.

import math as m

# Import module with alias.

from math import sqrt as square_root

# Import item with alias.


# ==========================================================
# SUMMARY
# ==========================================================

# • import is used to reuse code from modules.
# • A module is a Python file containing reusable code.
# • from ... import ... imports specific functions or objects.
# • as gives an imported module or object another name.
# • Python searches its module search path to locate imports.
# • Modules make programs organized and reusable.
# • Python normally loads a module only once during execution.
