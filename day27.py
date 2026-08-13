# ==========================================================
# PYTHON DAY 27
# FOR LOOP WITH ELSE
# ==========================================================


# ==========================================================
# WHAT IS FOR LOOP WITH ELSE?
# ==========================================================

# Definition:

'''In Python, an else block can be used with a for loop.

The else block executes when the for loop completes
normally without encountering a break statement.'''


# ==========================================================
# BASIC SYNTAX
# ==========================================================

# for variable in sequence:

    # loop body

# else:

    # else body


# ==========================================================
# BASIC EXAMPLE
# ==========================================================

for i in range(5):

    print(i)

else:

    print("Loop completed")

# Output:

# 0
# 1
# 2
# 3
# 4
# Loop completed


# ==========================================================
# WHY IS ELSE USED WITH FOR LOOP?
# ==========================================================

# The else block is useful when you want to execute
# some code after the loop finishes normally.

# It is especially useful when the loop contains
# a break statement.


# ==========================================================
# FOR LOOP WITH ELSE AND BREAK
# ==========================================================

for i in range(5):

    print(i)

    if i == 2:

        break

else:

    print("Loop completed")

# Output:

# 0
# 1
# 2

# The else block does NOT execute because
# the loop was stopped using break.


# ==========================================================
# FOR LOOP WITHOUT BREAK
# ==========================================================

for i in range(5):

    print(i)

else:

    print("Loop completed successfully")

# Output:

# 0
# 1
# 2
# 3
# 4
# Loop completed successfully


# ==========================================================
# SEARCHING FOR A NUMBER
# ==========================================================

numbers = [10, 20, 30, 40, 50]

for number in numbers:

    if number == 30:

        print("Number found")
        break

else:

    print("Number not found")

# Output:

# Number found

# Because break was executed,
# the else block was skipped.


# ==========================================================
# NUMBER NOT FOUND
# ==========================================================

numbers = [10, 20, 30, 40, 50]

for number in numbers:

    if number == 100:

        print("Number found")
        break

else:

    print("Number not found")

# Output:

# Number not found

# The loop completed normally,
# so the else block executed.


# ==========================================================
# CHECKING FOR A PRIME NUMBER
# ==========================================================

number = 7

for i in range(2, number):

    if number % i == 0:

        print("Not a prime number")
        break

else:

    print("Prime number")

# Output:

# Prime number

# No number from 2 to 6 divides 7,
# so break is never executed.
# Therefore, else executes.


# ==========================================================
# PRIME NUMBER EXAMPLE
# ==========================================================

number = 8

for i in range(2, number):

    if number % i == 0:

        print("Not a prime number")
        break

else:

    print("Prime number")

# Output:

# Not a prime number

# 8 is divisible by 2.
# break executes.
# Therefore, else does not execute.


# ==========================================================
# IMPORTANT ROLE OF BREAK
# ==========================================================

# No break:

for i in range(3):

    print(i)

else:

    print("Else executed")


# break:

for i in range(3):

    if i == 1:

        break

else:

    print("Else executed")

# In the second example,
# else does not execute.


# ==========================================================
# ELSE DOES NOT MEAN "IF LOOP CONDITION IS FALSE"
# ==========================================================

# This is an important point.

# The else block of a for loop executes when
# the loop finishes normally.

# It does NOT simply mean:

# "if the loop condition is false"


# ==========================================================
# FOR ELSE WITH LIST
# ==========================================================

names = ["Alice", "Bob", "Charlie"]

for name in names:

    if name == "Bob":

        print("Bob found")
        break

else:

    print("Bob not found")

# Output:

# Bob found


# ==========================================================
# FOR ELSE WITHOUT FINDING ELEMENT
# ==========================================================

names = ["Alice", "Charlie", "David"]

for name in names:

    if name == "Bob":

        print("Bob found")
        break

else:

    print("Bob not found")

# Output:

# Bob not found


# ==========================================================
# FOR ELSE WITH CONTINUE
# ==========================================================

for i in range(5):

    if i == 2:

        continue

    print(i)

else:

    print("Loop completed")

# Output:

# 0
# 1
# 3
# 4
# Loop completed

# continue does NOT prevent else from executing.

# Only break prevents the else block
# from executing.


# ==========================================================
# FOR ELSE WITH BREAK AND CONTINUE
# ==========================================================

for i in range(5):

    if i == 2:

        continue

    if i == 4:

        break

    print(i)

else:

    print("Loop completed")

# Output:

# 0
# 1
# 3

# break occurs at 4,
# so the else block does not execute.


# ==========================================================
# NESTED FOR LOOP WITH ELSE
# ==========================================================

for i in range(3):

    for j in range(2):

        print(i, j)

    else:

        print("Inner loop completed")


# The else belongs to the nearest for loop.


# ==========================================================
# IMPORTANT RULE
# ==========================================================

# for loop completes normally
#          ↓
#       ELSE RUNS

# for loop encounters break
#          ↓
#       ELSE SKIPPED


# ==========================================================
# FOR LOOP WITH ELSE — FLOW
# ==========================================================

for i in range(5):

    if i == 10:

        break

else:

    print("Loop completed")

# Flow:

# Start loop
#     ↓
# Check condition
#     ↓
# Break found?
#     ↓
# No
#     ↓
# Continue loop
#     ↓
# Loop finishes
#     ↓
# ELSE executes


# ==========================================================
# FOR LOOP WITH ELSE — BREAK FLOW
# ==========================================================

for i in range(5):

    if i == 2:

        break

else:

    print("Loop completed")

# Flow:

# Start loop
#     ↓
# i reaches 2
#     ↓
# break
#     ↓
# Loop stops
#     ↓
# ELSE is skipped


# ==========================================================
# QUICK REVISION
# ==========================================================

# for-else is a special Python feature.

# else executes when the loop completes normally.

# break prevents the else block from executing.

# continue does NOT prevent else from executing.

# It is commonly used for searching.

# It is also commonly used for prime-number checking.


# ==========================================================
# IMPORTANT DIFFERENCE
# ==========================================================

# break:

# Stops the loop completely.

# continue:

# Skips the current iteration
# and continues with the next iteration.

# else:

# Executes when the loop finishes normally.


# ==========================================================
# SUMMARY
# ==========================================================

#  Python allows else with a for loop.
#  else runs when the loop completes normally.
#  break prevents else from running.
#  continue does not prevent else from running.
#  for-else is useful for searching.
#  for-else is commonly used in prime-number checking.
