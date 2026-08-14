# ==========================================================
# PYTHON DAY 33
# VIRTUAL ENVIRONMENT & COMMANDS
# ==========================================================


# ==========================================================
# WHAT IS A VIRTUAL ENVIRONMENT?
# ==========================================================

# Definition:

'''A virtual environment is an isolated Python environment
that allows a project to have its own Python packages and
dependencies.

Each project can have its own separate environment.'''


# ==========================================================
# WHY IS A VIRTUAL ENVIRONMENT NEEDED?
# ==========================================================

'''Different projects may require different versions of
the same package.

A virtual environment keeps project dependencies separate.

Example:

Project A
    ↓
Package version 1

Project B
    ↓
Package version 2

Both projects can work independently.'''


# ==========================================================
# ADVANTAGES
# ==========================================================

# • Keeps dependencies isolated.
# • Prevents package conflicts.
# • Keeps projects organized.
# • Allows different package versions for different projects.
# • Makes projects easier to reproduce.


# ==========================================================
# CREATING A VIRTUAL ENVIRONMENT
# ==========================================================

# Command:

# python -m venv venv


# Here:

# python
# → Runs Python.

# -m venv
# → Runs Python's built-in virtual-environment module.

# venv
# → Name of the virtual environment.


# You can use another name:

# python -m venv myenv


# ==========================================================
# ACTIVATING VIRTUAL ENVIRONMENT — WINDOWS
# ==========================================================

# Command:

# venv\Scripts\activate


# After activation, you may see:

# (venv)

# at the beginning of the terminal.


# ==========================================================
# ACTIVATING VIRTUAL ENVIRONMENT — macOS / LINUX
# ==========================================================

# Command:

# source venv/bin/activate


# After activation:

# (venv)

# appears in the terminal.


# ==========================================================
# CHECKING PYTHON VERSION
# ==========================================================

# Command:

# python --version

# Example:

# Python 3.x.x


# ==========================================================
# CHECKING PIP VERSION
# ==========================================================

# Command:

# pip --version


# ==========================================================
# WHAT IS pip?
# ==========================================================

# Definition:

'''pip is Python's package installer.

It is used to install, update and remove Python packages.'''


# ==========================================================
# INSTALLING A PACKAGE
# ==========================================================

# Command:

# pip install package_name


# Example:

# pip install requests


# ==========================================================
# INSTALLING A SPECIFIC VERSION
# ==========================================================

# Command:

# pip install requests==2.31.0


# This installs the specified version of the package.


# ==========================================================
# UPGRADING A PACKAGE
# ==========================================================

# Command:

# pip install --upgrade requests


# This upgrades the package to a newer available version.


# ==========================================================
# UNINSTALLING A PACKAGE
# ==========================================================

# Command:

# pip uninstall requests


# pip will ask for confirmation.


# ==========================================================
# LISTING INSTALLED PACKAGES
# ==========================================================

# Command:

# pip list


# It displays packages installed
# in the current environment.


# ==========================================================
# SHOWING PACKAGE INFORMATION
# ==========================================================

# Command:

# pip show requests


# It displays information such as:

# • Package name
# • Version
# • Location
# • Dependencies


# ==========================================================
# REQUIREMENTS.TXT
# ==========================================================

# Definition:

'''requirements.txt is a file that contains the Python
packages required by a project.

Example:

requests==2.31.0
flask==3.0.0'''


# ==========================================================
# CREATING requirements.txt
# ==========================================================

# Command:

# pip freeze > requirements.txt


# This saves installed packages and their versions
# into requirements.txt.


# ==========================================================
# INSTALLING FROM requirements.txt
# ==========================================================

# Command:

# pip install -r requirements.txt


# This installs all packages listed in the file.


# ==========================================================
# DEACTIVATING VIRTUAL ENVIRONMENT
# ==========================================================

# Command:

# deactivate


# The (venv) label disappears from the terminal.


# ==========================================================
# VIRTUAL ENVIRONMENT WORKFLOW
# ==========================================================

# Step 1:

# python -m venv venv


# Step 2:

# Activate it.

# macOS / Linux:

# source venv/bin/activate

# Step 3:

# pip install package_name


# Step 4:

# pip freeze > requirements.txt


# Step 5:

# deactivate


# ==========================================================
# PROJECT STRUCTURE
# ==========================================================

# Example:

'''my_project/
│
├── venv/
│
├── main.py
│
└── requirements.txt


# venv contains the isolated environment.

# main.py contains the project code.

# requirements.txt contains project dependencies.'''


# ==========================================================
# SHOULD venv BE UPLOADED TO GITHUB?
# ==========================================================

'''Usually, no.

The virtual environment contains installed packages
and can be recreated using requirements.txt.

Instead of uploading venv:

• Add venv to .gitignore.
• Upload requirements.txt.'''


# ==========================================================
# .gitignore
# ==========================================================

# Example:

# venv/


# This tells Git to ignore the virtual environment folder.


# ==========================================================
# GLOBAL PYTHON VS VIRTUAL ENVIRONMENT
# ==========================================================

'''Global Python:

• Packages are installed for the general Python environment.
• Projects can share the same packages.
• Package conflicts can occur.

Virtual Environment:

• Packages are isolated for a project.
• Different projects can use different versions.
• Better for project development.'''


# ==========================================================
# IMPORTANT COMMANDS
# ==========================================================

# Create environment:

# python -m venv venv


# Activate — macOS/Linux:

# source venv/bin/activate

# Install package:

# pip install package_name


# Uninstall package:

# pip uninstall package_name


# List packages:

# pip list


# Package information:

# pip show package_name


# Save dependencies:

# pip freeze > requirements.txt


# Install dependencies:

# pip install -r requirements.txt


# Upgrade package:

# pip install --upgrade package_name


# Deactivate:

# deactivate


# ==========================================================
# QUICK REVISION
# ==========================================================

'''Virtual Environment:

An isolated Python environment for a project.

venv:

Python's built-in module for creating virtual environments.

pip:

Python package installer.

requirements.txt:

File containing project dependencies.

activate:

Enables the virtual environment.

deactivate:

Leaves the virtual environment.'''


# ==========================================================
# SUMMARY
# ==========================================================

# • Virtual environments isolate project dependencies.
# • venv is Python's built-in virtual-environment module.
# • pip is used to manage Python packages.
# • requirements.txt stores project dependencies.
# • venv should generally not be uploaded to GitHub.
# • .gitignore can be used to ignore the venv folder.
# • A virtual environment can be recreated whenever needed.


# ==========================================================
# DAY 33 COMPLETED
# ==========================================================