# Open Function
# 
# The open() function is used to either read content from, or write content to a file based on the argument we pass. It is a common file handling tool used in Python.
# 
# Syntax
# open(file, mode)

# Usage
f = open("demofile.txt", "r")


print(f.read())

# Parameters
# file - The path and name of the file.
# mode - A string, define which mode you want to open the file in:
        # "r" - Read - Default value. Opens a file for reading, error if the file does not exist.
        # "a" - Append - Opens a file for appending, creates the file if the file does not exist.
        # "w" - Write - Opens a file for writing, creates the file if the file does not exist.
        # "x" - Create - Creates the specified file, returns an error if the file exists. 
