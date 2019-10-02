"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

print('Command line arguments \n 👇')
for elem in sys.argv:
    print(elem)
print()

# if you want to exclude the file name
print('Command line arguments without filename \n 👇')
for (idx, elem) in enumerate(sys.argv):
    if idx != 0:
        print(elem)
print()

# Print out the OS platform you're using:
# YOUR CODE HERE

print('OS Platform \n 👇')
if sys.platform.startswith('freebsd'):
    print('FreeBSD')
elif sys.platform.startswith('linux'):
    print('Linux')
elif sys.platform == 'darwin':
    print('Mac OS X')
elif sys.platform == 'win32':
    print('Windows')
elif sys.platform == 'cygwin':
    print('Windows/Cygwin')
else:
    print(sys.platform)
print()

# Print out the version of Python you're using:
# YOUR CODE HERE
print('Python Version \n 👇')
print(f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} ")
print()

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print('Current Process ID \n 👇')
print(os.getpid())
print()

# Print the current working directory (cwd):
# YOUR CODE HERE
print('Current Working Directory \n 👇')
print(os.getcwd())
print()

# Print out your machine's login name
# YOUR CODE HERE
print('Login Name \n 👇')
print(os.getlogin())
